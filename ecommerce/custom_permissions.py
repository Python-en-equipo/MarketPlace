from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsStaffOrReadOnly(BasePermission):
    """
    The request is authenticated as staff, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user.is_staff)


class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has a `seller` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        try:
            return obj.seller.profile.email == request.user.email
        except Exception as e:
            print(e)
            return False
