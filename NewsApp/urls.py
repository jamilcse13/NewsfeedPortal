from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user-news/', views.user_news),
    # path('settings/', views.settings)
]