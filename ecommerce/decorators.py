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
        # seller = Seller.objects.get(profile__email=request.user.email)
        # print(seller.profile.email)
        # print(request.user.email)
        # print(product.seller.profile.email)

        if request.method == "GET":
            return function(request, *args, **kwargs)
        # en caso que sea otro verbo
        try:
            if request.user.email == product.seller.profile.email:
                return function(request, *args, **kwargs)
            raise PermissionDenied("No tienes los permisos para editar este producto")
        except Exception as e:
            print(e)
            raise PermissionDenied("No tienes los permisos para editar este producto")

    return wrapper_function
