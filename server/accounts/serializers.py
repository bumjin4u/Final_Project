from rest_framework import serializers
from articles.models import Article, Comment
from django.contrib.auth import get_user_model



class ArticleSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username', read_only=True)
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'username', 'like_count',)



class CommentSerializer(serializers.ModelSerializer):
    
    article = ArticleSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'content', 'article',)
        read_only_fields = ('article','user')



class UserSerializer(serializers.ModelSerializer):
    class FollowerSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id','username')

    comments = CommentSerializer(many=True, read_only=True)
    articles = ArticleSerializer(many=True, read_only=True)
    like_articles = ArticleSerializer(many=True, read_only=True)
    followings = serializers.IntegerField(source='followings.count', read_only=True)
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    followers = FollowerSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'followings', 'followers', 'comments', 'articles', 'like_articles','followers_count','followers')