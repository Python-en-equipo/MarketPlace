from django.shortcuts import redirect
from rest_framework.exceptions import PermissionDenied

from ecommerce.models import Product
from users.models import Seller


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
        seller = Seller.objects.get(profile__email=request.user.email)
        print(seller.profile.email)
        print(request.user.email)
        print(product.seller.profile.email)

        if request.method == "GET":
            return function(request, *args, **kwargs)
        elif request.user.email == product.seller.profile.email:
            return function(request, *args, **kwargs)
        raise PermissionDenied("No puedes editar este elemento")

    return wrapper_function


# def own_user_required(func):
#     @functools.wraps(func)
#     def wrapper(request, *args, **kwargs):
#         user = get_object_or_404(CustomUser, pk=int(kwargs['pk']))

#         if request.method == 'GET':
#             return func(request, *args, **kwargs)
#         if request.user == user:
#             return func(request, *args, **kwargs)
#         raise PermissionDenied("Usted no es el propietario de este objeto")

#     return wrapper
