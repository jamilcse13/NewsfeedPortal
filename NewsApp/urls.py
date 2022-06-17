from django.urls import path
from . import views

urlpatterns = [
path('<str:heading>/<str:name>/', views.index)
]