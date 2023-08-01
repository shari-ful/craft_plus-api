from rest_framework import serializers
from .models import Product

class GetProduct(serializers.ModelSerializer):
    class Meta:
        model = Product


class CreateProduct(serializers.ModelSerializer):
    title = serializers.CharField(read_only=False, required=True)
    title = serializers.CharField(read_only=False, required=True)
    price = serializers.FloatField(read_only=False, required=True)
    brand = serializers.CharField(read_only=False, required=True)
    category = serializers.ChoiceField(read_only=False, required=True)
    discount = serializers.IntegerField(read_only=False, required=True)
    description = serializers.CharField(read_only=False, required=True)
    digital = serializers.BooleanField(read_only=False, required=True)
    store = serializers.CharField(read_only=False, required=True)
    quantity = serializers.IntegerField(read_only=False, required=True)
    class Meta:
        model = Product


class UpdateProduct(serializers.ModelSerializer):
    class Meta:
        model = Product

