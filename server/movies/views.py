# Create your views here.
from .models import Movie, Genre
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import MovieListSerializer, MovieSerializer, TaglineListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(["GET"])
def searchMovie(request, query):
    movies = Movie.objects.filter(title__contains=query) | Movie.objects.filter(original_title__contains=query)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movieList(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movieDetail(request, movie_id):
    movie = get_object_or_404(Movie,id=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def Bmovie(request):
    movies = Movie.objects.filter(vote_average__gt=6) & Movie.objects.filter(vote_average__lt=7) & Movie.objects.filter(vote_count__gt=200) & Movie.objects.filter(vote_count__lt=500)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def SleepMovie(request):
    movies = Movie.objects.filter(runtime__gt=180)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def taglines(request):
    movies = Movie.objects.filter(tagline__isnull=False)
    serializer = TaglineListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def animation(request):
    movies = Movie.objects.filter(genres__in=[16])
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
