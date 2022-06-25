from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser, Seller
from .permissions import IsOwnerSellerPermission, IsOwnerUserPermission
from .serializers import SellerSerializer, UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsOwnerUserPermission, IsAuthenticated]

    def update(self, request, pk):
        user = self.get_object()

        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SellerCreateAPIView(CreateAPIView):
    serializer_class = SellerSerializer
    permission_classes = [IsAuthenticated]


class SellerRetirieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerSellerPermission]
