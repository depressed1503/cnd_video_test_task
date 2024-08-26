from rest_framework import serializers
from .models import CityModel

class CityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = ['name', 'lattitude', 'longitude']