from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("user/<int:pk>", views.user_detail, name="user-detail"),
    path("signup/", views.user_create, name="user-create"),
    path("seller/<int:pk>", views.seller_detail, name="seller-detail"),
]
