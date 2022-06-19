from django.shortcuts import render
import requests
import environ
from django.http import HttpResponse

# Create your views here.
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


def index(request):
    API_KEY = env('NEWS_API_KEY')
    BASE_NEWS_API = env('BASE_NEWS_API')
    country = request.GET.get('country')
    source = request.GET.get('source')

    if country:
        url = f'{BASE_NEWS_API}/top-headlines?country={country}&apiKey={API_KEY}'
    elif source:
        url = f'{BASE_NEWS_API}/top-headlines?sources={source}&apiKey={API_KEY}'
    else:
        url = f'{BASE_NEWS_API}/top-headlines?country=us&apiKey={API_KEY}'

    crypto_news = requests.get(url).json()
    articles = crypto_news['articles']

    context = {'articles': articles}

    return render(request, 'newsfeed/index.html', context)


def settings(request):
    return render(request, 'newsfeed/settings.html')