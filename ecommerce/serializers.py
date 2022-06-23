from rest_framework import serializers

from ecommerce.models import Category, Image, Product
from users.models import Seller


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.title", read_only=False)
    seller = serializers.CharField(source="seller.seller_name", read_only=True)
    # seller = SellerSerializer()

    class Meta:
        model = Product
        # AÑADIR SELLER SERIALIZER
        fields = ("id", "slug", "title", "description", "price", "category", "stock", "seller")

        extra_kwargs = {
            "id": {"read_only": True},
            "slug": {"read_only": True},
            "title": {"required": True},
            "category": {"required": True},
            "description": {"required": True},
            "price": {"required": True},
            "stock": {"required": True},
        }

    def create(self, validated_data):
        print(validated_data)
        category = validated_data.pop("category")
        category_title = Category.objects.get(title=category["title"])
        print(category_title)
        email = self.context["request"].user
        try:
            seller_email = Seller.objects.get(profile__email=email)
            print(seller_email)
            product = Product.objects.create(**validated_data, category=category_title, seller=seller_email)
            return product
        except Seller.DoesNotExist:
            raise serializers.ValidationError("Crea antes una tienda para poder publicar productos")

    def update(self, instance, validated_data):
        category = validated_data.pop("category")
        category_title = Category.objects.get(title=category["title"])
        print(category_title)
        instance.category = category_title
        return super().update(instance, validated_data)


class CategorySerializer(serializers.ModelSerializer):
    # products = serializers.StringRelatedField(many=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "slug", "title", "products"]

        extra_kwargs = {"id": {"read_only": True}, "slug": {"read_only": True}
        }

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["product"]
