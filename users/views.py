from django.shortcuts import get_object_or_404
from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from config.settings import SWAGGER_SETTINGS
from users.decorators import own_user_required
from users.models import CustomUser, Seller
from users.serializers import SellerSerializer, UserSerializer


@swagger_auto_schema(
    method="post",
    operation_description="Create new user (Authentication required)",
    request_body=UserSerializer,
    responses={
        201: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(title="Email", type=openapi.TYPE_STRING),
                "first_name": openapi.Schema(title="First Name", type=openapi.TYPE_STRING),
                "last_name": openapi.Schema(title="Last Name", type=openapi.TYPE_STRING),
            },
        )
    },
)
@api_view(["POST"])
def user_create(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="get",
    operation_description="Get user by id (Authentication required)",
    responses={
        200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(title="Email", type=openapi.TYPE_STRING),
                "first_name": openapi.Schema(title="First Name", type=openapi.TYPE_STRING),
                "last_name": openapi.Schema(title="Last Name", type=openapi.TYPE_STRING),
            },
        )
    },
)
@swagger_auto_schema(
    methods=["put"],
    operation_description="Update user by id (Authentication required)",
    responses={
        200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(title="Email", type=openapi.TYPE_STRING),
                "first_name": openapi.Schema(title="First Name", type=openapi.TYPE_STRING),
                "last_name": openapi.Schema(title="Last Name", type=openapi.TYPE_STRING),
            },
        )
    },
)
@swagger_auto_schema(
    methods=["delete"],
    operation_description="Delete user by id (Authentication required)",
    responses={
        200: openapi.Schema(
            type=openapi.TYPE_OBJECT, properties={"message": openapi.Schema(title="Message", type=openapi.TYPE_STRING)}
        )
    },
)
@api_view(["GET", "PUT", "DELETE"])
@own_user_required
def user_detail(request, pk):
    if request.method == "GET":
        user = get_object_or_404(CustomUser, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == "PUT" or request.method == "PATCH":
        user = get_object_or_404(CustomUser, pk=pk)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user = get_object_or_404(CustomUser, pk=pk)
        user.delete()
        return Response({"message": "Usuario eliminado con exito"}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def seller_detail(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    serializer = SellerSerializer(seller)
    return Response(serializer.data)
