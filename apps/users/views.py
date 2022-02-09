from django.shortcuts import render, redirect
from django.core.cache import cache
from .forms import VendorForm
from django.contrib.auth.decorators import login_required 

# from django.contrib.auth import authenticate, login, logout
# from apps.ecommerce.decorators import unauthenticated_user
# from django.contrib import messages



def delete_home_cache():
    """borra las keys de los valores en cache de la home"""
    cache.delete_many(["views.decorators.cache.cache_header..17abf5259517d604cc9599a00b7385d6.en-us.UTC",
                        "views.decorators.cache.cache_page..GET.17abf5259517d604cc9599a00b7385d6.d41d8cd98f00b204e9800998ecf8427e.en-us.UTC",])


@login_required
def vendor_register(request):
    """ registro disponible para clientes, debe estar registrado en la plataforma para acceder a este registro"""
    vendor_form = VendorForm()
    if request.method == "POST":
        vendor_form = VendorForm(request.POST)
        if vendor_form.is_valid():
            vendor = vendor_form.save(commit=False)
            vendor.user = request.user
            vendor.save()
            return redirect("ecommerce:home")
    else:
        vendor_form = VendorForm()

    return render(request, "users/vendor_register.html", {"vendor_form": vendor_form})
