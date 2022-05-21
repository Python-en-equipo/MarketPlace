from django.urls import path
from ecommerce import views

urlpatterns = [
    path('', views.api_root),
    path('products/', views.product_list, name='product-list'),
    path('products/<str:slug>', views.product_detail, name='product-detail'),
    path('categories/', views.category_list, name='category-list'),
    path('categories/<str:slug>', views.category_detail, name='category-detail'),
]
   




# ANTES DE QUE FUERA API
# from .views import (
#     category,
#     home,
#     product_create,
#     product_deletion,
#     product_detail_view,
#     product_edit_view,
# )

# # no borrar porque los templates usan la appname
# app_name = "ecommerce"

# urlpatterns = [
#     path("", home, name="home"),
#     path("category/<slug:category_slug>", category, name="category"),
#     path("new/", product_create, name="product-create"),
#     path("edit/<int:product_id>", product_edit_view, name="product-edit"),
#     path("detail/<int:product_id>", product_detail_view, name="product-detail"),
#     path("delete/<int:product_id>", product_deletion, name="product-delete"),

# ]
