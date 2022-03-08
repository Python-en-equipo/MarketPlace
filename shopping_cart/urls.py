from django.urls import path

from .views import store_view

app_name = 'shopping_cart'

urlpatterns = [
  path("add_product/",store_view, name="add_product")
]
