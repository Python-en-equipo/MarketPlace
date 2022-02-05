from django.contrib import admin    
from django.contrib.auth.admin import UserAdmin
from .models import User, Seller

admin.site.register(User, UserAdmin)
admin.site.register(Seller)