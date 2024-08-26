from rest_framework import serializers
from .models import CityModel
from .utils import get_longitude_and_latitude


class CityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = ['name', 'lattitude', 'longitude']

    def create(self, validated_data):
        validated_data['lattitude'], validated_data['longitude'] = get_longitude_and_latitude(validated_data['name'])
        return CityModel(**validated_data)