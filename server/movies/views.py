# Create your views here.
from .models import Actor, Movie, Genre

from .serializers import MovieListSerializer, ActorListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(["GET"])
def searchMovie(request, query):
    movies = Movie.objects.filter(title__contains=query) | Movie.objects.filter(original_title__contains=query)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def searchActor(request, query):
    actors = Actor.objects.filter(name__contains=query)
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)