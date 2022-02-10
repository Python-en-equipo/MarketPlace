from django.conf import settings
from django.core.cache import cache

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import redirect, render



from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_page
from django.views.decorators.http import condition


from .forms import ImageForm, ProductForm
from .models import Image, Product


CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)

def delete_home_cache():
    """borra las keys de los valores en cache de la home"""
    cache.delete_many(["views.decorators.cache.cache_header..17abf5259517d604cc9599a00b7385d6.en-us.UTC",
                        "views.decorators.cache.cache_page..GET.17abf5259517d604cc9599a00b7385d6.d41d8cd98f00b204e9800998ecf8427e.en-us.UTC",])

def home(request):  
    products = Product.objects.exclude(price__lt=50)
    return render(request, "ecommerce/home.html", {"products": products})


@login_required
def product_create(request):
    if request.user.seller:
        product_form = ProductForm()
        image_form = ImageForm()
        if request.method == "POST":
            product_form = ProductForm(request.POST)
            image_form = ImageForm(request.POST, request.FILES)
            if product_form.is_valid() and image_form.is_valid():
                product = product_form.save(commit=False)
                product.seller = request.user.seller
                product.save()
                image = image_form.save(commit=False)
                image.product = product
                image.save()
                delete_home_cache()
                return redirect("ecommerce:home")
    else:
        return redirect("ecommerce:home")
    
    return render(request, "ecommerce/product_edit.html", {"product_form": product_form, "image_form": image_form})


@login_required
def product_edit_view(request, product_id):
    instance_product = Product.objects.get(id=product_id)
    try:
        instance_image = Image.objects.get(product__id=product_id)
    except Image.DoesNotExist:
        instance_image = None
    product_form = ProductForm(request.POST or None, instance=instance_product)
    image_form = ImageForm(request.POST, request.FILES, instance=instance_image)
    if product_form.is_valid() and image_form.is_valid():
        product = product_form.save()
        image = image_form.save(commit=False)
        image.product = product
        image.save()
        delete_home_cache()
        return redirect("ecommerce:home")
    elif product_form.is_valid():
        product = product_form.save()
        return redirect("ecommerce:home")

    return render(request, "ecommerce/product_edit.html", {"product_form": product_form, "image_form": image_form})


def product_detail_view(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "ecommerce/product_detail.html", {"product": product})


@login_required
def product_deletion(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        messages.success(request, f"{product} was succesfully deleted")
        product.delete()
        delete_home_cache()
        return redirect("ecommerce:home")
    return render(request, "ecommerce/product_delete.html", {"product": product})