from email.policy import default
from enum import unique
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from phonenumber_field.modelfields import PhoneNumberField


# class Client(models.Model):
#     PAYMENT_CHOICES = [
#         ("Tarjeta de crédito", 'credit card'),
#         ("Tarjeta de débito", 'debit card'),
#         ("Paypal", 'paypal')
#     ]
#     client = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_staff = models.BooleanField(default=False)
#     address = models.CharField(max_length=150)
#     payment_method = models.CharField(max_length=30, choices=PAYMENT_CHOICES, default=None)
#     newsletter_suscribed = models.BooleanField(default=False)

class GeneralProfile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    personalized_password = models.CharField(max_length=15, default="fake_pass")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Employee(models.Model):
    user = models.OneToOneField(GeneralProfile, on_delete=models.CASCADE, related_name="user_key", primary_key=True)
    joined_at = models.DateTimeField(auto_now=True)
    phone_number = PhoneNumberField(unique=True, blank=True)
    address = models.CharField(max_length=170)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"