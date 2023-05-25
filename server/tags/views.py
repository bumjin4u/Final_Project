from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Tag
from movies.models import Movie
from .serializers import TagSerializer, TagListSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

@api_view(["GET","POST"]) # 태그 조회, 생성
@permission_classes([IsAuthenticatedOrReadOnly])
def tagList(request):
    if request.method=="GET":
        tags = Tag.objects.all()
        serializer = TagListSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = TagListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(["GET","POST"]) # 태그된 영화들 조회, 추가
def tagDetail(request,tag_id):
    tag = get_object_or_404(Tag,id=tag_id)
    if request.method == "GET":
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        pk = request.data.get('movie_id')
        movie = Movie.objects.get(pk=pk)
        if tag.movies.filter(pk=pk).exists():
            msg = {'message':'이미 존재하는 영화입니다.'}
            return Response(msg, status=status.HTTP_208_ALREADY_REPORTED)
        tag.movies.add(movie)
        return Response(status=status.HTTP_201_CREATED)
