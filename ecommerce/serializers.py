from os import read

from django.utils.text import slugify
from rest_framework import serializers

from ecommerce.models import Category, Image, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["slug", "title"]


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        # TODO AÑADIR SELLER SERIALIZER
        fields = ("id", "title", "slug", "description", "price", "category", "stock")


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["product"]
