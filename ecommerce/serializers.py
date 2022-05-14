from os import read
from ecommerce.models import Category, Product, Image
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
            model = Category
            fields = [
                "title", "slug"
            ]


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        # TODO AÑADIR SELLER SERIALIZER
        fields = [
            "title", "description",
            "price", "category", "slug",
            "stock"
        ]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "product"
        ]


