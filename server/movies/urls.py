from django.urls import path
from . import views

urlpatterns = [
    path('search/movie/<str:query>/', views.searchMovie),
]
