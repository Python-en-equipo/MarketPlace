from os import read
from ecommerce.models import Category, Product, Image
from rest_framework import serializers
from django.utils.text import slugify


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
            model = Category
            fields = [
                "title", "slug"
            ]


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    title_slug = serializers.SerializerMethodField()

    def get_title_slug(self, instance):
        return slugify(instance.title)

    class Meta:
        model = Product
        # TODO AÑADIR SELLER SERIALIZER
        fields = [
            "title_slug", "title", "description",
            "price", "category",
            "stock"
        ]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "product"
        ]


