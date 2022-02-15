from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

# no borrar porque los templates usan la appname
app_name = "ecommerce"

urlpatterns = [
    path("", cache_page(60 * 15)(home), name="home"),
    path("categoria/<str:category_slug>/", category, name="category"),
    path("new/", product_create, name="product-create"),
    path("edit/<int:product_id>", product_edit_view, name="product-edit"),
    path("detail/<int:product_id>", product_detail_view, name="product-detail"),
    path("delete/<int:product_id>", product_deletion, name="product-delete"),

]
