import requests
from django.conf import settings
from transformers import pipeline

# Initialize summarizer (T5 model)
summarizer = pipeline('summarization', model='t5-small', tokenizer='t5-small')

NEWS_API_URL = 'https://newsapi.org/v2/'


def fetch_latest_news():
    url = f"{NEWS_API_URL}top-headlines"
    params = {
        'country': 'us',
        'apiKey': settings.NEWS_API_KEY,
        'pageSize': 10,
    }
    response = requests.get(url, params=params)
    return response.json().get('articles', [])


def fetch_news_by_query(query):
    url = f"{NEWS_API_URL}everything"
    params = {
        'q': query,
        'apiKey': settings.NEWS_API_KEY,
        'pageSize': 10,
        'language': 'en',
    }
    response = requests.get(url, params=params)
    return response.json().get('articles', [])


def summarize_text(text, max_length=60, min_length=20):
    # T5 expects a prefix "summarize: "
    input_text = "summarize: " + text
    summary = summarizer(input_text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text'] if summary else text 