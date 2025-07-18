
from django.urls import path
from .views import BlogAPI

urlpatterns = [
    path('blogs/', BlogAPI.as_view()),          
    path('blogs/<int:pk>/', BlogAPI.as_view()),
]
