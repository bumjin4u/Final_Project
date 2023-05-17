from django.shortcuts import render
from .models import Movie, Genre, Actor
# Create your views here.

def movieList(request):
    movies = Movie.objects.all()

def genreList(request):
    pass

def actorList(request):
    pass