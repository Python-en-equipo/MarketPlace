from django.contrib import admin
from .models import Vendor, Profile
from django.contrib.auth.admin import UserAdmin

admin.site.register(Profile)
admin.site.register(Vendor)