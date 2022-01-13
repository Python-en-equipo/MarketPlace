from django.urls import path

from . import views

app_name = "ecommerce"
urlpatterns = [
    path("home/", views.show_my_page, name="home"),
    path("edit/<int:product_id>", views.product_edit_view, name="product-edit"),
    path("new/", views.product_create, name="product-create"),
    path("detail/<int:product_id>", views.product_detail_view, name="product-detail"),
    path("delete/<int:product_id>", views.product_deletion, name="product-delete"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
