from django.shortcuts import render
from .forms import ProductForm, ImageForm
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.cache import cache_page

from .models import Image, Product

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

#cache_page(CACHE_TTL)
def show_my_page(request):
    queryset = Product.objects.exclude(price__lt=50)
    return render(request, 'ecommerce/base.html', {'result': queryset})

def product_create(request):
    product_form = ProductForm()
    image_form = ImageForm()
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save()
            image = image_form.save(commit=False)
            image.product = product
            image.save()
            return HttpResponseRedirect(reverse('ecommerce:home'))

    return render(request, 'ecommerce/product_edit.html', {'product_form': product_form, 'image_form': image_form})


def product_edit_view(request, id):
    instance_product = Product.objects.get(id=id)
    try:
        instance_image = Image.objects.get(product__id=id)
    except Image.DoesNotExist:
        instance_image = None
    product_form = ProductForm(request.POST or None, instance=instance_product)
    image_form = ImageForm(request.POST, request.FILES, instance=instance_image)
    if product_form.is_valid():
            product = product_form.save()
            return HttpResponseRedirect(reverse('ecommerce:home'))
    elif product_form.is_valid() and image_form.is_valid():
        product = product_form.save()
        image = image_form.save(commit=False)
        image.product = product
        image.save()
        return HttpResponseRedirect(reverse('ecommerce:home'))
    
    return render(request, 'ecommerce/product_edit.html', {'product_form': product_form, 'image_form': image_form})

def product_detail_view(request, id):
    product = Product.objects.get(id=id)

    return render(request, 'ecommerce/product_detail.html', {'product': product})