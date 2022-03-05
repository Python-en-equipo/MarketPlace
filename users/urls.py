from django.urls import path

from . import views

# no borrar porque los templates usan la appname
app_name = "users"

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("seller_register/", views.seller_register, name="seller_register"),
    path("user_panel/", views.user_panel, name="user_panel"),
    path("user_edit/", views.user_modify_view, name="user_edit"),
]
