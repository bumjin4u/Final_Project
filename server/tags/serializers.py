from rest_framework import serializers
from .models import Tag
from movies.models import Movie

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name')

class TagSerializer(serializers.ModelSerializer):
    
    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id','title','original_title','poster_path')
    
    movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ('movies',)