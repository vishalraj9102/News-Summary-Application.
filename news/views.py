from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import UserRegisterSerializer, UserLoginSerializer, SavedArticleSerializer
from .models import SavedArticle
from .services import fetch_latest_news, fetch_news_by_query, summarize_text
from rest_framework.permissions import IsAuthenticated

# User Registration
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

# User Login (returns JWT via SimpleJWT)
from rest_framework_simplejwt.tokens import RefreshToken
class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# Get latest summarized news
class LatestNewsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        articles = fetch_latest_news()
        summarized = []
        for article in articles:
            content = article.get('content') or article.get('description') or ''
            summary = summarize_text(content) if content else ''
            summarized.append({
                'title': article.get('title'),
                'summary': summary,
                'url': article.get('url'),
                'source': article.get('source', {}).get('name', ''),
            })
        return Response(summarized)

# Search and summarize news
class SearchNewsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        query = request.query_params.get('q', '')
        if not query:
            return Response({'detail': 'Query parameter "q" is required.'}, status=400)
        articles = fetch_news_by_query(query)
        summarized = []
        for article in articles:
            content = article.get('content') or article.get('description') or ''
            summary = summarize_text(content) if content else ''
            summarized.append({
                'title': article.get('title'),
                'summary': summary,
                'url': article.get('url'),
                'source': article.get('source', {}).get('name', ''),
            })
        return Response(summarized)

# Save a news article
class SaveNewsView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = SavedArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Get saved news articles for the authenticated user
class SavedNewsListView(generics.ListAPIView):
    serializer_class = SavedArticleSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return SavedArticle.objects.filter(user=self.request.user).order_by('-created_at')
