from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Seller


class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "password1", "password2")


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email")


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ("seller_name",)
