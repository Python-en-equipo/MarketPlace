from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

app_name = "users"

urlpatterns = [
    path("<int:pk>", views.UserRetrieveUpdateDestroyAPIView.as_view(), name="user-detail"),
    path("", views.UserCreateAPIView.as_view(), name="user-create"),
    path("token/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "seller/<int:pk>", views.SellerRetirieveUpdateDestroyAPIView.as_view(), name="seller-detail"
    ),
    path("seller/", views.SellerCreateAPIView.as_view(), name="seller-create"),
]
