from django.contrib import admin

from .models import Employee, GeneralProfile

admin.site.register(GeneralProfile)
admin.site.register(Employee)