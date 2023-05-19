from django.urls import path
from . import views

urlpatterns = [
    path('search/movie/<str:query>/', views.searchMovie),
    path('search/actor/<str:query>/', views.searchActor),
]
