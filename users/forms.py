from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Seller


class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "password1", "password2")


class UserEditForm(UserChangeForm):
    description = forms.CharField(widget=forms.Textarea(
		attrs={
			'class':'form-control w-100',
			'rows':'3',
			}))
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email")


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ("seller_name",)