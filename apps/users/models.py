from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=170, null=True, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    phone_number = PhoneNumberField(unique=True, blank=True) 
    def __str__(self):
        return self.email


class Vendor(models.Model):
    user  = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="vendor", primary_key=True)
    name_vendor = models.CharField(max_length=50, null=True, blank=True)
    #is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name_vendor}"
