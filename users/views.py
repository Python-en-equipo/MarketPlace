from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
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


@api_view(['GET'])
def user_detail(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def seller_detail(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    serializer = SellerSerializer(seller)
    return Response(serializer.data)
