from django.urls import path

from .views import add_product_cart, delete_product_cart, list_products_cart, remove_product_cart

app_name = "shopping_cart"

urlpatterns = [
    path("", list_products_cart, name="home"),
    path("add_product/<int:product_id>", add_product_cart, name="add_product"),
    path("remove_product/<int:product_id>", remove_product_cart, name="remove_product"),
    path("delete_product/<int:product_id>", delete_product_cart, name="delete_product"),
]
