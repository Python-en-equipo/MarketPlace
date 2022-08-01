from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from ecommerce.custom_permissions import IsOwnerOrReadOnly, IsStaffOrReadOnly
from ecommerce.models import Category, Product
from ecommerce.serializers import CategorySerializer, ProductSerializer


class APIRootView(APIView):
    def get(self, request):
        data = {
            "ecommerce": reverse("ecommerce:product-list", request=request),
            "category": reverse("ecommerce:category-list", request=request),
        }
        return Response(data)


class ProductList(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        queryset = Product.objects.all().order_by("id")
        category_name = self.request.query_params.get("category")
        seller_name = self.request.query_params.get("seller")
        if category_name is not None:
            category_name = category_name.capitalize()
            queryset = queryset.filter(category__title=category_name)
        elif seller_name is not None:
            seller_name = seller_name.capitalize()
            queryset = queryset.filter(seller__seller_name=seller_name)

        return queryset


class ProductDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "slug"
    permission_classes = [IsOwnerOrReadOnly]


class CategoryList(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by("id")
    permission_classes = [IsStaffOrReadOnly]


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "slug"
    permission_classes = [IsStaffOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.products.count() > 0:
            return Response({"error": "La colección no se puede eliminar porque tiene productos"})
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
