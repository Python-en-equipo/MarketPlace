from os import read
from ecommerce.models import Category, Product, Image
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(read_only=True, view_name='product-category')
    seller = serializers.HyperlinkedRelatedField(read_only=True, view_name='product-seller')

    class Meta:
        model = Product
        fields = [
            "category", "seller", "title",
            "description","price", "slug",
            "stock", "is_available",
        ]

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(read_only=True, view_name='product-image')

    class Meta:
        model = Image
        fields = [
            "product", "image_location"
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(read_only=True, view_name='product-category')

    class Meta:
        model = Category
        fields = [
            "product", "title", "slug"
        ]