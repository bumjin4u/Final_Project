from rest_framework import serializers
from .models import Article, Comment
from movies.models import Movie
from django.contrib.auth import get_user_model


class ArticleListSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username', read_only=True)
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'username', 'like_count',)
        

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article','user', 'username')


class ArticleSerializer(serializers.ModelSerializer): # POST


    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'like_users', )

class ArticleDetailSerializer(serializers.ModelSerializer): # GET
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model=Movie
            fields = ('id','title','original_title','poster_path')

    like_count = serializers.IntegerField(source='like_users.count', read_only=True)
    movie = MovieSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'user','title','content','created_at','updated_at', 'movie', 'like_count', 'username')
        read_only_fields = ('user', 'movie')


class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'like_users')




