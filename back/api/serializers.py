from rest_framework import serializers
from .models import CityModel
from .utils import get_longitude_and_latitude


class CityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = ['name', 'latitude', 'longitude']

    def create(self, validated_data):
        validated_data['latitude'], validated_data['longitude'] = get_longitude_and_latitude(validated_data['name'])
        instance = CityModel(**validated_data)
        instance.save()
        return instance
