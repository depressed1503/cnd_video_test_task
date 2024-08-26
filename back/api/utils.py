from django.db.models import F, FloatField
from django.db.models.functions import Sqrt, Power
from django.db.models import Value
from .models import CityModel
import requests


def get_two_closest_cities(lat, lon):
    # Haversine formula components
    cities = CityModel.objects.annotate(
        distance=Sqrt(
            Power(F('latitude') - Value(lat), 2) + 
            Power(F('longitude') - Value(lon), 2)
        )
    ).order_by('distance')[:2]

    return list(cities)


def get_longitude_and_latitude(name: str):
            # api call to get lattitude and longitude
        response = requests.get(f'https://api.geoapify.com/v1/geocode/search?text={name}&apiKey=b0867caece604e9e903f272a4366c33b')
        response.raise_for_status()
        try:
            data = response.json()
        except requests.JSONDecodeError:
            data = None
        lat = None
        lon = None
        if data and len(data['features']):
            lat = data['features'][0]['properties']['lat']
            lon = data['features'][0]['properties']['lon']

        return lat, lon