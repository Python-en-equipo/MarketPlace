from django.contrib import admin

from .models import Image, Product, Category

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Category)
