from django.shortcuts import render
from rest_framework import generics, decorators, response
from .models import CityModel
from .serializers import CityModelSerializer
from .utils import get_two_closest_cities


class CityModelCreateAPIView(generics.CreateAPIView):
    queryset = CityModel.objects.all()
    serializer_class = CityModelSerializer

class CityModelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CityModel.objects.all()
    serializer_class = CityModelSerializer
    
@decorators.api_view(['GET'])
def get_closest_cities(request):
	cities = get_two_closest_cities(int(request.data['latitude']), int(request.data['longitude']))
	return response.Response(CityModelSerializer(cities, many=True).data)
