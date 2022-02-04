from .forms import UserForm, EmployeeForm, GeneralFormUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from apps.ecommerce.decorators import unauthenticated_user
from django.contrib import messages
from django.core.cache import cache


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
            user = form.cleaned_data.get("username")
            messages.success(request, f"{user} was succesfully created")

            return redirect("users:login")
    print(form)
    return render(request, "users/register.html", {"user_registration": form})


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


def employee_register(request):
    user_form = GeneralFormUser()
    employee_form = EmployeeForm()
    if request.method == "POST":
        user_form = GeneralFormUser(request.POST)
        employee_form = EmployeeForm(request.POST)
        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save()
            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()
            return redirect("ecommerce:home")
    return render(request, "users/employee_register.html", { "user_form": user_form, "employee_form": employee_form})
