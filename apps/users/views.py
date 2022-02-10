from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from apps.ecommerce.decorators import unauthenticated_user
from django.contrib import messages
from django.core.cache import cache
from django.contrib.auth.decorators import login_required 
from .forms import SellerForm


def delete_home_cache():
    """borra las keys de los valores en cache de la home"""
    cache.delete_many(["views.decorators.cache.cache_header..17abf5259517d604cc9599a00b7385d6.en-us.UTC",
                        "views.decorators.cache.cache_page..GET.17abf5259517d604cc9599a00b7385d6.d41d8cd98f00b204e9800998ecf8427e.en-us.UTC",])


@login_required
def vendor_register(request):
    """ registro disponible para clientes, debe estar registrado en la plataforma para acceder a este registro"""
    seller_form = SellerForm()
    if request.method == "POST":
        seller_form = SellerForm(request.POST)
        if seller_form.is_valid():
            vendor = seller_form.save(commit=False)
            vendor.profile = request.user
            vendor.save()
            return redirect("ecommerce:home")
            
    return render(request, "users/seller_register.html", { "seller_form": seller_form})
