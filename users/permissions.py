from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerUserPermission(BasePermission):
    message = "You do not have permission to manipulate user given"

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj == request.user


class IsOwnerSellerPermission(BasePermission):
    message = "You do not have permission to do this"

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.seller == request.user
