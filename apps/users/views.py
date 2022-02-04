from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from apps.ecommerce.decorators import unauthenticated_user
from django.contrib import messages
from .forms import UserForm
# Create your views here.




@unauthenticated_user
def register_view(request):
    form = UserForm
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, f"{user} was succesfully created")

            return redirect("login")
    print(form)
    return render(request, "users/register.html", {"user_registration": form})


@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or password is incorrect.")

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)

    return redirect("login")
