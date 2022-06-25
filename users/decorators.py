import functools

from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

from users.models import CustomUser


def own_user_required(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=int(kwargs["pk"]))

        if request.method == "GET":
            return func(request, *args, **kwargs)
        if request.user == user:
            return func(request, *args, **kwargs)
        raise PermissionDenied("Usted no es el propietario de este objeto")

    return wrapper
