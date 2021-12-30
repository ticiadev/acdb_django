from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Villager, Personality
from .serializers import VillagerSerializer, PersonalitySerializer


class VillagerList(APIView):

    def get(self, request):
        villager1 = Villager.objects.all()
        serializer = VillagerSerializer(villager1, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


class VillagerDetail(APIView):

    def get(self, request, id):
        villager1 = Villager.objects.get(id=id)
        serializer = VillagerSerializer(villager1)
        # print(serializer)
        return Response(serializer.data)
