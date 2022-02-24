<<<<<<< HEAD
from django.contrib import admin

from .models import Image, Product

admin.site.register(Product)
admin.site.register(Image)
=======
from django.contrib import admin

from .models import Image, Product, Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Image)
>>>>>>> redis
