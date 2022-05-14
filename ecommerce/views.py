from multiprocessing import context
from django.shortcuts import get_object_or_404
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, action, renderer_classes
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from ecommerce.models import Product, Category
from ecommerce.serializers import ProductSerializer, CategorySerializer
from rest_framework.request import Request
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

# LINK PARA LA API
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'ecommerce': reverse('product-list', request=request, format=format),
        'category': reverse('category-list', request=request, format=format),
    })


@api_view(['GET'])
def product_list(request):
    queryset = Product.objects.select_related('category').all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view()
def category_list(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response('ok')
