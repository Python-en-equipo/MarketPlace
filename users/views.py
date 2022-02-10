from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ecommerce.decorators import unauthenticated_user

from django.contrib import messages
from django.core.cache import cache
from .forms import UserForm, SellerForm

from django.contrib.auth.decorators import login_required 



def delete_home_cache():
    """borra las keys de los valores en cache de la home"""
    cache.delete_many(["views.decorators.cache.cache_header..17abf5259517d604cc9599a00b7385d6.en-us.UTC",
                        "views.decorators.cache.cache_page..GET.17abf5259517d604cc9599a00b7385d6.d41d8cd98f00b204e9800998ecf8427e.en-us.UTC",])


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
def seller_register(request):
    """ registro disponible para clientes, debe estar registrado en la plataforma para acceder a este registro"""
    if request.user.seller == False :
        seller_form = SellerForm()
        if request.method == "POST":
            seller_form = SellerForm(request.POST)
            if seller_form.is_valid():
                seller = seller_form.save(commit=False)
                seller.profile = request.user
                seller.save()
                return redirect("ecommerce:home")
    else:
        return redirect("ecommerce:home")
    return render(request, "users/seller_register.html", { "seller_form": seller_form})
