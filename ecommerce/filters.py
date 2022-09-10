from django_filters.rest_framework import FilterSet

from ecommerce.models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {"category": ["exact"], "seller": ["exact"], "price": ["gt", "lt"]}
