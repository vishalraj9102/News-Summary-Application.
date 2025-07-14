from django.urls import path
from .views import (
    UserRegisterView, UserLoginView,
    LatestNewsView, SearchNewsView,
    SaveNewsView, SavedNewsListView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/register/', UserRegisterView.as_view(), name='register'),
    path('auth/login/', UserLoginView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('news/latest/', LatestNewsView.as_view(), name='latest_news'),
    path('news/search/', SearchNewsView.as_view(), name='search_news'),
    path('news/save/', SaveNewsView.as_view(), name='save_news'),
    path('news/saved/', SavedNewsListView.as_view(), name='saved_news'),
] 