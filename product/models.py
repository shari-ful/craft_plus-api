from django.db import models

# Create your models here.


class Catagory(models.Model):
    name = models.CharField(max_length=50, null=True)
class Product(models.Model):
    title = models.CharField(max_length=200, null=True)
    price = models.FloatField(max_length=200, null=True)
    discount = models.IntegerField(null=True, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image_1 = models.ImageField(blank=True)
    image_2 = models.ImageField(blank=True, null=True)
    image_3 = models.ImageField(blank=True, null=True)
    image_4 = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def image1URL(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return url
