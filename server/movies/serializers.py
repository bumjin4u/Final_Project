from rest_framework import serializers
from .models import Movie, Genre
from actors.models import Actor

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','original_title','poster_path', 'runtime')


class MovieSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'
        
    class ActorListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('id','name','profile_path')
    
    actors = ActorListSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

class TaglineListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','tagline')