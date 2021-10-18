from django.shortcuts import render
from .models import Product

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

queryset = Product.objects.filter(price__gt=50)

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def show_my_page(request):
    return render(request, 'base.html', {'result': queryset})