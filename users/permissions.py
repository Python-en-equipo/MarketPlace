from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerPermission(BasePermission):
    message = "You do not have permission to manipulate user given"

    def has_permission(self, request, view):

        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj == request.user
