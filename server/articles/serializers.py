from rest_framework import serializers
from .models import Article, Comment
from ..movies.models import Movie
from django.contrib.auth import get_user_model


class ArticleListSerializer(serializers.ModelSerializer):

    username = serializers.CharField(wource='user.username', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article','user')


class ArticleSerializer(serializers.ModelSerializer): # POST
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)

class ArticleDetailSerializer(serializers.ModelSerializer): # GET
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model=Movie
            fields = ('id','title','original_title','poster_path')

    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Article
        fields = ('user','title','content','create_at','updated_at',)
        read_only_fields = ('user',)

class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)




