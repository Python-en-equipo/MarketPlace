from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from ecommerce.decorators import unauthenticated_user

from django.contrib import messages

from users.models import CustomUser, Seller
from .forms import UserForm, SellerForm, UserEditForm
from ecommerce.models import Product


def delete_home_cache():
    """borra las keys de los valores en cache de la home"""
    cache.delete_many(["views.decorators.cache.cache_header..17abf5259517d604cc9599a00b7385d6.en-us.UTC",
                       "views.decorators.cache.cache_page..GET.17abf5259517d604cc9599a00b7385d6.d41d8cd98f00b204e9800998ecf8427e.en-us.UTC", ])


@unauthenticated_user
def register_view(request):
    form = UserForm
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("email")
            messages.success(request, f"{user} was succesfully created")
            return redirect("users:login")

    return render(request, "users/register.html", {"user_registration": form})


@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("ecommerce:home")
        else:
            messages.info(request, "Email or password is incorrect.")

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("users:login")

@login_required
def user_panel(request):
    if hasattr(request.user, 'seller'):
        products = Product.objects.filter(seller= request.user.seller)
        ctx = {"products": products}
        return render(request, "users/user_panel.html", ctx)
    else:
        return render(request, "users/user_panel.html")



@login_required
def seller_register(request):
    """ registro disponible para clientes, debe estar registrado en la plataforma para acceder a este registro"""
    """ hay que preveer de que alguien ya registrado como vendedor no se pueda volver a entrar a este registro"""
    seller_form = SellerForm()
    if request.method == "POST":
        seller_form = SellerForm(request.POST)
        if seller_form.is_valid():
            seller = seller_form.save(commit=False)
            seller.profile = request.user
            seller.save()
            return redirect("ecommerce:home")
    
    return render(request, "users/seller_register.html", {"seller_form": seller_form})

@login_required
def user_modify_view(request):
    try:
        instance_seller = Seller.objects.get(profile__id=request.user.id)
    except Seller.DoesNotExist:
        instance_seller = None
    user_form = UserEditForm(instance=request.user)
    seller_form = SellerForm(instance=instance_seller)
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        seller_form = SellerForm(request.POST or None, instance=instance_seller)
        if user_form.is_valid() and seller_form.is_valid():
            custom_user = user_form.save()
            seller = seller_form.save(commit=False)
            seller.profile_name = custom_user
            seller.save()
            return redirect("users:user_panel")
        elif user_form.is_valid():
            user_form.save()
            return redirect("users:user_panel")

    return render(request, "users/users_edit.html", {"user_form": user_form, "seller_form": seller_form})



# def product_edit_view(request, product_id):
#     instance_product = Product.objects.get(id=product_id)
#     try:
#         instance_image = Image.objects.get(product__id=product_id)
#     except Image.DoesNotExist:
#         instance_image = None
#     product_form = ProductForm(request.POST or None, instance=instance_product)
#     image_form = ImageForm(request.POST, request.FILES, instance=instance_image)
#     if product_form.is_valid() and image_form.is_valid():
#         product = product_form.save()
#         image = image_form.save(commit=False)
#         image.product = product
#         image.save()
#         delete_home_cache()
#         return redirect("ecommerce:home")

#    elif product_form.is_valid():
#         product = product_form.save()
#         return redirect("ecommerce:home")

#     return render(request, "ecommerce/product_edit.html", {"product_form": product_form, "image_form": image_form})
