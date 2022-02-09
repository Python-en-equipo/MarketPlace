from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Vendor


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', "email", "password1", "password2"]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('__all__')


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ("__all__")
