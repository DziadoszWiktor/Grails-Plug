#serializer get informations from database and puts it into a json file for front-end use

from rest_framework import serializers
from .models import Product, Categories

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "size",
            "brand",
            "get_absolute_url",
            "get_image",
            "get_thumbnail",
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Categories
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )