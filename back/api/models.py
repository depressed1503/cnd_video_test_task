from typing import Any
from django.db import models


class CityModelManager(models.Manager):
    def create(self, **kwargs: Any) -> Any:
        # api call to get lattitude and longitude
        return super().create(**kwargs)
    
class CityModel(models.Model):
    name = models.CharField(max_length=255)
    lattitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    objects = CityModelManager
