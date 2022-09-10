from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser, Seller
from .permissions import IsOwnerSellerPermission, IsOwnerUserPermission
from .serializers import CreateSellerSerializer, SellerSerializer, UserCreateSerializer, UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsOwnerUserPermission, IsAuthenticated]


class SellerCreateAPIView(CreateAPIView):
    serializer_class = CreateSellerSerializer
    permission_classes = [IsAuthenticated]


class SellerRetirieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerSellerPermission]
