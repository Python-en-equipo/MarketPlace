from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import CustomUser, Seller


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name", "password", "password2")
        extra_kwargs = {
            "email": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        # validate password
        if validated_data["password"] != validated_data["password2"]:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden"})

        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])

        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "first_name", "last_name")
        extra_kwargs = {"email": {"required": True}, "first_name": {"required": True}, "last_name": {"required": True}}

    # update user
    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)

        instance.save()

        return instance


class CreateSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ("seller_name",)

    def create(self, validated_data):
        user = CustomUser.objects.get(id=self.context["request"].user.id)
        print(user)

        try:
            seller = Seller.objects.create(profile=user, seller_name=validated_data["seller_name"])

            return seller
        except ObjectDoesNotExist:
            error = {"message": "The user is already a seller"}
            raise serializers.ValidationError(error)


class SellerSerializer(serializers.ModelSerializer):
    profile = UserSerializer(read_only=True)

    class Meta:
        model = Seller
        fields = ("seller_name", "profile")
