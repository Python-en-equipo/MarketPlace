from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class GeneralProfile(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Seller(models.Model):
    user = models.OneToOneField(GeneralProfile, on_delete=models.CASCADE, related_name="user_key", primary_key=True)
    joined_at = models.DateTimeField(auto_now=True)
    phone_number = PhoneNumberField(unique=True, blank=True)
    address = models.CharField(max_length=170)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"