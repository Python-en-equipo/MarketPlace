from django.contrib import admin

from .models import Image, Product

admin.site.register(Product)
admin.site.register(Image)
