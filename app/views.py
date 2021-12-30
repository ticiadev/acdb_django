from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import villagers
from .serializers import villagersSerializer

class villagerlist(APIView):

     def get(self, request):
         villager1 = villagers.objects.all()
         serializer = villagersSerializer(villager1, many= True)
         return Response(serializer.data)

class villagerdetail(APIView):

     def get(self, request, id):
         villager = villagers.objects.get(id=id)
         serializer = villagersSerializer(villager)
         print(serializer)
         return Response(serializer.data)

     def post(self, request, id):
         pass
