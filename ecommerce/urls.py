from django.urls import path

from ecommerce import views

app_name = "ecommerce"

urlpatterns = [
    path("", views.APIRootView.as_view()),
    path("products/", views.ProductList.as_view(), name="product-list"),
    path("products/<str:slug>", views.ProductDetail.as_view(), name="product-detail"),
    path("categories/", views.CategoryList.as_view(), name="category-list"),
    path("categories/<str:slug>", views.CategoryDetail.as_view(), name="category-detail"),
]
