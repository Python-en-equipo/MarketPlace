from django.urls import path
from .views import home, product_create, product_detail_view, product_edit_view, product_deletion, category

# no borrar porque los templates usan la appname
app_name = "ecommerce"

urlpatterns = [
    path("", home, name="home"),
    path("category/<slug:category_slug>", category, name="category"),
    path("new/", product_create, name="product-create"),
    path("edit/<int:product_id>", product_edit_view, name="product-edit"),
    path("detail/<int:product_id>", product_detail_view, name="product-detail"),
    path("delete/<int:product_id>", product_deletion, name="product-delete"),

]
