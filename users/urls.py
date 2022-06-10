from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

app_name = "users"

urlpatterns = [
    path("<int:pk>", views.user_detail, name="user-detail"),
    path("", views.user_create, name="user-create"),
    path('token/', TokenObtainPairView.as_view(), name="login"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path("seller/<int:pk>", views.seller_detail, name="seller-detail"),
]
