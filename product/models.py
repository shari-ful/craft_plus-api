from django.db import models
from store.models import Store
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    icon = models.ImageField(upload_to='media/category/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
class Product(models.Model):
    title = models.CharField(max_length=200, null=True)
    price = models.FloatField(blank=True, null=True)
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, default=0)

    image_1 = models.ImageField(upload_to='media/product/', blank=True)
    image_2 = models.ImageField(upload_to='media/product/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='media/product/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='media/product/', blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def image1URL(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return url
