from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

app_name = "users"

urlpatterns = [
    path("users/<int:pk>", views.UserRetrieveUpdateDestroyAPIView.as_view(), name="user-detail"),
    path("users/", views.UserCreateAPIView.as_view(), name="user-create"),
    path("users/token/", TokenObtainPairView.as_view(), name="login"),
    path("users/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("sellers/<int:pk>", views.SellerRetirieveUpdateDestroyAPIView.as_view(), name="seller-detail"),
    path("sellers/", views.SellerCreateAPIView.as_view(), name="seller-create"),
]
