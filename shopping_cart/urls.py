from django.urls import path

from .views import list_products_cart, add_product_cart

app_name = 'shopping_cart'

urlpatterns = [
  path("", list_products_cart, name="home"),
  path("add_product/<int:product_id>",add_product_cart, name="add_product"),
  # path("remove_product/",store_view, name="delete_product"),
  # path("update_product/",store_view, name="update_product"),
]
