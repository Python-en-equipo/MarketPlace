from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

app_name = "users"

urlpatterns = [
    path("user/<int:pk>", views.user_detail, name="user-detail"),
    path("signup/", views.user_create, name="user-create"),
    path("seller/<int:pk>", views.seller_detail, name="seller-detail"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
