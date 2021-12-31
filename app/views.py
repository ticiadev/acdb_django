from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Villager, Personality, Coffee, Game, Amiibo, House, \
    Furniture
from .serializers import VillagerSerializer, PersonalitySerializer, \
    CoffeeSerializer, GameSerializer, AmiiboSerializer, HouseSerializer, \
    FurnitureSerializer


class VillagerViewSet(viewsets.ModelViewSet):
    """Allow villagers to be shown or edited."""
    queryset = Villager.objects.all()
    serializer_class = VillagerSerializer


class PersonalityList(APIView):

    def get(self, request):
        personality = Personality.objects.all()
        serializer = PersonalitySerializer(personality, many=True)
        return Response(serializer.data)
