from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Vendor, Profile




class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Vendor)
