from django.urls import path

from . import views

# no borrar porque los templates usan la appname
app_name = "users"

urlpatterns = [
    path("user/<int:pk>", views.user_detail, name="user_detail"),
    path("signup/", views.user_create, name="user_create"),
]
