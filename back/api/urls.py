from django.urls import path, include
from rest_framework import routers
from .views import CityModelRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('city/', CityModelRetrieveUpdateDestroyAPIView.as_view())
]