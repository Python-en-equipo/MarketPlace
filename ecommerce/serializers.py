from os import read
from ecommerce.models import Category, Product, Image
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(),
        view_name= 'category-detail',
    )
    class Meta:
        model = Product
        fields = [
            "category", "title",
            "description","price", "slug",
            "stock", "is_available",
        ]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "product"
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
            model = Category
            fields = [
                "title", "slug"
            ]