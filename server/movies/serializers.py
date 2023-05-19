from rest_framework import serializers
from .models import Actor, Movie, Genre

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','original_title','poster_path')

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id','name','profile_path')