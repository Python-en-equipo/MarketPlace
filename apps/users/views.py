from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from apps.ecommerce.decorators import unauthenticated_user
from django.contrib import messages
from django.core.cache import cache
from .forms import CustomUserCreationForm


def delete_home_cache():
    """borra las keys de los valores en cache de la home"""
    cache.delete_many(["views.decorators.cache.cache_header..17abf5259517d604cc9599a00b7385d6.en-us.UTC",
                        "views.decorators.cache.cache_page..GET.17abf5259517d604cc9599a00b7385d6.d41d8cd98f00b204e9800998ecf8427e.en-us.UTC",])


@unauthenticated_user
def register_view(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("first_name")
            messages.success(request, f"{user} was succesfully created")
            return redirect('account_login')
    print(form)
    return render(request, "account/signup.html", {"user_registration": form})


@unauthenticated_user
def login_view(request):
    delete_home_cache()
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


# def logout_view(request):
#     logout(request)

#     return redirect("users:login")


# def seller_register(request):
#     user_form = GeneralFormUser()
#     employee_form = SellerForm()
#     if request.method == "POST":
#         user_form = GeneralFormUser(request.POST)
#         employee_form = SellerForm(request.POST)
#         if user_form.is_valid() and employee_form.is_valid():
#             user = user_form.save()
#             employee = employee_form.save(commit=False)
#             employee.user = user
#             employee.save()
#             return redirect("ecommerce:home")
#     return render(request, "users/seller_register.html", { "user_form": user_form, "employee_form": employee_form})
