from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import redirect, render

from .decorators import unauthenticated_user
from .forms import ImageForm, ProductForm, UserForm
from .models import Image, Product

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


# cache_page(CACHE_TTL)
def show_my_page(request):
    queryset = Product.objects.exclude(price__lt=50)
    return render(request, "ecommerce/base.html", {"result": queryset})


@unauthenticated_user
def register_view(request):
    form = UserForm
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, f"{user} was succesfully created")

            return redirect("ecommerce:login")

    return render(request, "ecommerce/register.html", {"user_registration": form})


@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("ecommerce:home")
        else:
            messages.info(request, "Username or password is incorrect.")

    return render(request, "ecommerce/login.html")


def logout_view(request):
    logout(request)

    return redirect("ecommerce:login")


@staff_member_required
def product_create(request):
    product_form = ProductForm()
    image_form = ImageForm()
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save()
            image = image_form.save(commit=False)
            image.product = product
            image.save()
            return redirect("ecommerce:home")

    return render(request, "ecommerce/product_edit.html", {"product_form": product_form, "image_form": image_form})


@staff_member_required
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


@staff_member_required
def product_deletion(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        messages.success(request, f"{product} was succesfully deleted")
        product.delete()
        return redirect("ecommerce:home")
    return render(request, "ecommerce/product_delete.html", {"product": product})
