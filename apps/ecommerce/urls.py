from django.urls import path

from .views import show_my_page,  product_edit_view, product_create, product_detail_view, product_deletion

app_name = "ecommerce"

urlpatterns = [
    path("", show_my_page, name="home"),
    path("edit/<int:product_id>", product_edit_view, name="product-edit"),
    path("new/", product_create, name="product-create"),
    path("detail/<int:product_id>", product_detail_view, name="product-detail"),
    path("delete/<int:product_id>", product_deletion, name="product-delete"),

]
