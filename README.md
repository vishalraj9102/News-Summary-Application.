# News Summary API

A Django REST Framework backend API for fetching, summarizing, and saving news articles using AI-powered summarization.

## Features

- 🔍 Fetch latest news from NewsAPI
- 🔎 Search news by keywords
- 🤖 AI-powered news summarization using free transformers library
- 🔐 JWT authentication for secure access
- 💾 Save and retrieve favorite news articles
- 📱 RESTful API endpoints

## Tech Stack

- **Backend**: Django 4.2.7
- **API**: Django REST Framework 3.14.0
- **Authentication**: JWT (djangorestframework-simplejwt)
- **AI Summarization**: Transformers library with T5 model
- **News Source**: NewsAPI.org
- **Database**: SQLite (default)

## Prerequisites

- Python 3.8+
- pip (Python package installer)

## Installation & Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd news-summary-api
```

### 2. Create virtual environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
NEWS_API_KEY=your-newsapi-key-here
```

### 5. Get NewsAPI Key
1. Go to [https://newsapi.org/](https://newsapi.org/)
2. Sign up for a free account
3. Get your API key
4. Add it to the `.env` file

### 6. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create superuser (optional)
```bash
python manage.py createsuperuser
```

### 8. Run the development server
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/refresh/` - Refresh JWT token

### News Endpoints
- `GET /api/news/latest/` - Get latest summarized news
- `GET /api/news/search/?q=term` - Search and summarize news
- `POST /api/news/save/` - Save a news article
- `GET /api/news/saved/` - Get saved news articles

## API Usage Examples

### 1. Register a new user
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123", "email": "test@example.com"}'
```

### 2. Login
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

### 3. Get latest news (with JWT token)
```bash
curl -X GET http://127.0.0.1:8000/api/news/latest/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### 4. Search news
```bash
curl -X GET "http://127.0.0.1:8000/api/news/search/?q=technology" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### 5. Save a news article
```bash
curl -X POST http://127.0.0.1:8000/api/news/save/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Article Title", "content": "Article content...", "url": "https://example.com", "source": "Example News"}'
```

### 6. Get saved articles
```bash
curl -X GET http://127.0.0.1:8000/api/news/saved/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## Project Structure

```
Deskos/
├── manage.py
├── requirements.txt
├── .env                    # Environment variables
├── .gitignore
├── README.md
├── db.sqlite3             # Database (auto-generated)
├── news_summary_api/      # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── news/                  # Main app (all features)
    ├── __init__.py
    ├── models.py          # SavedArticle model
    ├── serializers.py     # User and article serializers
    ├── services.py        # News API and AI summarization
    ├── views.py           # All API endpoints
    ├── urls.py            # URL routing
    ├── admin.py
    ├── apps.py
    ├── tests.py
    └── migrations/
``


