# Create your views here.
from .models import Actor
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import ActorListSerializer, ActorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["GET"])
def searchActor(request, query):
    actors = Actor.objects.filter(name__contains=query)
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def actorList(request):
    actors = get_list_or_404(Actor)
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def actorDetail(request, actor_id):
    actor = get_object_or_404(Actor,id=actor_id)
    serializer = ActorSerializer(actor)
    return Response(serializer.data, status=status.HTTP_200_OK)