from rest_framework import serializers
from .models import Actor, Movie, Genre

class GenreSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id',)

    movies = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id',)
    movies = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('id',)
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id',)
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
