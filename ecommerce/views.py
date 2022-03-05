from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ImageForm, ProductForm
from .models import Category, Image, Product

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


def seller_check(user):
    return hasattr(user, 'seller')


def home(request):
    products = Product.objects.all()
    product_count = products.count()

    return render(request, "ecommerce/home.html", {"products": products, "product_count": product_count})

def category(request, category_slug=None):
    category_instance = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category_instance)
    product_count = products.count()

    return render(request, "ecommerce/home.html", {"products": products, "product_count": product_count})


@user_passes_test(seller_check)
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
                return redirect("ecommerce:home")
    else:
        return redirect("ecommerce:home")

    return render(request, "ecommerce/product_edit.html", {"product_form": product_form, "image_form": image_form})


@user_passes_test(seller_check)
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
        return redirect("ecommerce:home")

        
    elif product_form.is_valid():
        product = product_form.save()
        return redirect("ecommerce:home")

    return render(request, "ecommerce/product_edit.html", {"product_form": product_form, "image_form": image_form})


def product_detail_view(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "ecommerce/product_detail.html", {"product": product})


@user_passes_test(seller_check)
@login_required
def product_deletion(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        messages.success(request, f"{product} was succesfully deleted")
        product.delete()
        return redirect("ecommerce:home")
    return render(request, "ecommerce/product_delete.html", {"product": product})
