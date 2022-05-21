from django.shortcuts import redirect
from rest_framework.exceptions import PermissionDenied

from ecommerce.models import Product


def unauthenticated_user(function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("ecommerce:home")
        else:
            return function(request, *args, **kwargs)

    return wrapper_function


def user_is_seller(function):
    def wrapper_function(request, *args, **kwargs):
        print(kwargs)
        product = Product.objects.get(slug=kwargs["slug"])
        if request.method == "GET":
            return function(request, *args, **kwargs)
        elif request.user == product.seller:
            return function(request, *args, **kwargs)
        raise PermissionDenied("No puedes editar este elemento")

    return wrapper_function
