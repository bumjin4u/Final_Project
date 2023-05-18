from django.shortcuts import render
from .models import Movie, Genre, Actor
from .serializers import MovieSerializer, GenreSerializer, ActorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def movieList(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    # if serializer.is_valid(raise_exception=True):
    #     print("통과")
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def genreList(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    # if serializer.is_valid(raise_exception=True):
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def actorList(request):
    actors = Actor.objects.all()
    serializer = ActorSerializer(actors, many=True)
    # if serializer.is_valid(raise_exception=True):
    return Response(serializer.data, status=status.HTTP_200_OK)