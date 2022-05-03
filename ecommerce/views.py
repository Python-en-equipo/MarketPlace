from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import permissions, generics
from ecommerce.models import Product
from ecommerce.serializers import ProductSerializer


# LINK PARA LA API
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'ecommerce': reverse('product-list', request=request, format=format),
        
    })
    

# GENERIC CLASS BASED VIEWS
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]