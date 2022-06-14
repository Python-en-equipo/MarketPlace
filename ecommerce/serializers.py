from rest_framework import serializers

from ecommerce.models import Category, Image, Product


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)
  

    class Meta:
        model = Category
        fields = ["slug", "title", "products"]


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()


    class Meta:
        model = Product
        # AÑADIR SELLER SERIALIZER
        fields = ("id", "slug", "title", "description", "price", "category", "stock")

        extra_kwargs = {
            'id': {'read_only': True},
            'slug': {'read_only': True},
            'title': {'required': True},
            'category': {'required': True},
            'description': {'required': True},
            'price': {'required': True},
            'stock': {'required': True},
        }
        

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["product"]
