import imp
from .forms import  UserForm, CustomProfileForm, VendorForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from apps.ecommerce.decorators import unauthenticated_user
from django.contrib import messages
from django.core.cache import cache

from django.contrib.auth.decorators import login_required 


from .models import Profile



def delete_home_cache():
    """borra las keys de los valores en cache de la home"""
    cache.delete_many(["views.decorators.cache.cache_header..17abf5259517d604cc9599a00b7385d6.en-us.UTC",
                        "views.decorators.cache.cache_page..GET.17abf5259517d604cc9599a00b7385d6.d41d8cd98f00b204e9800998ecf8427e.en-us.UTC",])

@unauthenticated_user
def login_view(request):
    delete_home_cache()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("ecommerce:home")
        else:
            messages.info(request, "Username or password is incorrect.")

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("users:login")




@unauthenticated_user
def register_view(request):
    form = UserForm
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} was succesfully created")
            Profile.objects.create(user=user)
            return redirect("users:login")      

    print(form)
    return render(request, "users/register.html", {"user_registration": form})






# @login_required
# def vendor_register(request):
#     """ registro disponible para clientes, debe estar registrado en la plataforma para acceder a este registro"""
#     user_form = GeneralFormUser()
#     vendor_form = VendorForm()
#     if request.method == "POST":
#         user_form = GeneralFormUser(request.POST)
#         vendor_form = VendorForm(request.POST)
#         if user_form.is_valid() and vendor_form.is_valid():
#             user = user_form.save()
#             vendor = vendor_form.save(commit=False)
#             vendor.user = user
#             vendor.save()
#             return redirect("ecommerce:home")
#     return render(request, "users/vendor_register.html", { "user_form": user_form, "vendor_form": vendor_form})
