# Create your views here.
from .models import Actor

from .serializers import ActorListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["GET"])
def searchActor(request, query):
    actors = Actor.objects.filter(name__contains=query)
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)