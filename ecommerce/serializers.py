from os import read
from ecommerce.models import Category, Product, Image
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
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


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(read_only=True, view_name='product-category')

    class Meta:
        model = Category
        fields = [
            "product", "title", "slug"
        ]