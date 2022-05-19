from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import CustomUser, Seller
from users.serializers import SellerSerializer, UserSerializer


@api_view(['POST'])
def user_create(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):
    if request.method == 'GET':
        user = get_object_or_404(CustomUser, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        user = get_object_or_404(CustomUser, pk=pk)

        if user == request.user:
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        raise PermissionDenied("Usted no es el propietario de este objeto")
    elif request.method == 'DELETE':
        user = get_object_or_404(CustomUser, pk=pk)
        if user == request.user:
            user.delete()
            return Response({"message": "Usuario eliminado con exito"}, status=status.HTTP_200_OK)
        raise PermissionDenied("Usted no es el propietario de este objeto")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def seller_detail(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    serializer = SellerSerializer(seller)
    return Response(serializer.data)
