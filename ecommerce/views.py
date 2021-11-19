from django.shortcuts import render
from .forms import ProductForm
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.cache import cache_page

from .models import Product

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# @cache_page(CACHE_TTL)
def show_my_page(request):
    queryset = Product.objects.exclude(price__lt=50)
    return render(request, 'ecommerce/base.html', {'result': queryset})

def product_create(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save()
        # form = ProductForm()
        return HttpResponseRedirect(reverse('ecommerce:product-detail', kwargs={'id': product.id}))

    return render(request, 'ecommerce/product_edit.html', {'form': form})

def product_edit_view(request, id):
    obj = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        # form = ProductForm()
        return HttpResponseRedirect(reverse('ecommerce:home'))
    
    return render(request, 'ecommerce/product_edit.html', {'form': form})

def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'ecommerce/product_detail.html', {'product': product})