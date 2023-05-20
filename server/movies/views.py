# Create your views here.
from .models import Movie
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import MovieListSerializer, MovieSerializer
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
    get_object_or_404
    movie = get_object_or_404(Movie,id=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)