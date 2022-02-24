<<<<<<< HEAD
from django.urls import path

from . import views

app_name = "ecommerce"
urlpatterns = [
    path("", views.show_my_page, name="home"),
    path("edit/<int:product_id>", views.product_edit_view, name="product-edit"),
    path("new/", views.product_create, name="product-create"),
    path("detail/<int:product_id>", views.product_detail_view, name="product-detail"),
    path("delete/<int:product_id>", views.product_deletion, name="product-delete"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
=======
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
>>>>>>> redis
