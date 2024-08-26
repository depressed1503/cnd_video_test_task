from django.shortcuts import render
from rest_framework import generics
from .models import CityModel
from .serializers import CityModelSerializer


class CityModelCreateAPIView(generics.CreateAPIView):
    queryset = CityModel.objects.all()
    serializer_class = CityModelSerializer

class CityModelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CityModel.objects.all()
    serializer_class = CityModelSerializer