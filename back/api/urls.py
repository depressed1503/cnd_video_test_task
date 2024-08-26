from django.urls import path, include
from rest_framework import routers
from .views import CityModelRetrieveUpdateDestroyAPIView, CityModelCreateAPIView, get_closest_cities


urlpatterns = [
    path('city/update_delete/<int:pk>/', CityModelRetrieveUpdateDestroyAPIView.as_view()),
    path('city/create/', CityModelCreateAPIView.as_view()),
    path('closest_cities/', get_closest_cities)
]
