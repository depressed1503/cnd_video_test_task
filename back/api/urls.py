from django.urls import path, include
from rest_framework import routers
from .views import CityModelRetrieveUpdateDestroyAPIView, CityModelCreateAPIView


urlpatterns = [
    path('city/update_delete/<int:pk>/', CityModelRetrieveUpdateDestroyAPIView.as_view()),
    path('city/create/', CityModelCreateAPIView.as_view()),
]