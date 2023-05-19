# Create your views here.
from .models import Movie

from .serializers import MovieListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(["GET"])
def searchMovie(request, query):
    movies = Movie.objects.filter(title__contains=query) | Movie.objects.filter(original_title__contains=query)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)