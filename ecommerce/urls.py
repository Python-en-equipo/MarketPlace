from django.urls import path

from .views import home,  product_edit_view, product_create, product_detail_view, product_deletion

# no borrar porque los templates usan la appname
app_name = "ecommerce"

urlpatterns = [
    path("", home, name="home"),
<<<<<<< HEAD:ecommerce/urls.py
    path("edit/<int:product_id>", product_edit_view, name="product-edit"),
=======
>>>>>>> f05a6c44dcb73ead5b8033d62261eb2477088ec2:apps/ecommerce/urls.py
    path("new/", product_create, name="product-create"),
    path("edit/<int:product_id>", product_edit_view, name="product-edit"),
    path("detail/<int:product_id>", product_detail_view, name="product-detail"),
    path("delete/<int:product_id>", product_deletion, name="product-delete"),

]
