from django.urls import path
from . import views

# no borrar porque los templates usan la appname
app_name = "users"

urlpatterns = [
    # path("register/", views.register_view, name="register"),
    # path("login/", views.login_view, name="login"),
    # path("logout/", views.logout_view, name="logout"),
    # path("new-seller/", views.seller_register, name="seller-register"),
]
