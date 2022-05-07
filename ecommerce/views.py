from multiprocessing import context
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, action, renderer_classes
from rest_framework.response import Response
from rest_framework import permissions, generics, status
from ecommerce.models import Product, Category
from ecommerce.serializers import ProductSerializer, CategorySerializer
from rest_framework.request import Request
from django.http import HttpRequest
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

# LINK PARA LA API
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'ecommerce': reverse('product-list', request=request, format=format),
    })

@api_view()
def product_list(request):
    return Response('ok')


@api_view()
def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   
    
