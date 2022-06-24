from django.shortcuts import get_object_or_404
from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CustomUser, Seller
from .permissions import IsOwnerPermission
from .serializers import SellerSerializer, UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    permission_classes = [IsOwnerPermission, IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def update(self, request, pk):
        user = self.get_object()

        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def seller_detail(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    serializer = SellerSerializer(seller)
    return Response(serializer.data)
