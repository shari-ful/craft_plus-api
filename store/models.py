from django.db import models
from.utils import *

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100, blank=True)
    type = models.CharField(choices=STORE_TYPE ,max_length=2)

    address_1 = models.CharField(max_length=200, blank=True, null=True)
    address_2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(choices=CITY_LIST, max_length=2)
    country = models.CharField(choices=COUNTRY_LIST, max_length=2)

    # create_by = models.ForeignKey()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    @property
    def avatarURL(self):
        try:
            url = self.avatar.url
        except:
            url = ''
        return url

class Location(models.Model):
    area = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(choices=COUNTRY_LIST, max_length=2)
    city = models.CharField(choices=CITY_LIST, max_length=2)
