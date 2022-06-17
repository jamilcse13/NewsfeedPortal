from django.shortcuts import render
import requests
import environ
from django.http import HttpResponse

# Create your views here.
env = env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

def index(request):
    API_KEY = env('NEWS_API_KEY')

    url = 'https://newsapi.org/v2/everything?q=Apple&from=2022-06-17&sortBy=popularity&apiKey='+API_KEY
    crypto_news = requests.get(url).json()
    a = crypto_news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        mylist = zip(title, desc, img)
    
    context = {'mylist': mylist}

    return render(request, 'index.html', context)