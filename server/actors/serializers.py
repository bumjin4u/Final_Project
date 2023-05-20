from rest_framework import serializers
from .models import Actor
from movies.models import Movie

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id','name','profile_path')

class ActorSerializer(serializers.ModelSerializer):

    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id','title','original_title','poster_path')

    movies = MovieListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Actor
        fields = '__all__'