from django.urls import path
from . import views
urlpatterns = [
    path('', views.movieList),
    path('genres/', views.genreList),
    path('actors/', views.actorList),
]
