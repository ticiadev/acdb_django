from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import villager
from .serializers import villagerSerializer

class villagerlist(APIView):

     def get(self, request):
         villager1 = villager.objects.all()
         serializer = villagerSerializer(villager1, many= True)
         return Response(serializer.data)

class villagerdetail(APIView):

     def get(self, request, id):
         villager = villager.objects.get(id=id)
         serializer = villagerSerializer(villager)
         print(serializer)
         return Response(serializer.data)

     def post(self, request, id):
         pass
