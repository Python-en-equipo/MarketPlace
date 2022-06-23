
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    """
    The request is authenticated as staff, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user.is_staff
        )

# class IsAuthenticatedOrReadOnly(BasePermission):
#     """
#     The request is authenticated as a user, or is a read-only request.
#     """

#     def has_permission(self, request, view):
#         return bool(
#             request.method in SAFE_METHODS or
#             request.user and
#             request.user.is_authenticated
#         )

class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # product = Product.objects.get(title=obj, seller)
        # email = product.objects.filter(seller)
        # print("si sirve el filtrado", type(product))
        # print(obj.seller)
        if request.method in SAFE_METHODS:
            return True
        # Only seller of the product can edit.
        try:
            return obj.seller.profile.email == request.user.email
        except:
            return False

