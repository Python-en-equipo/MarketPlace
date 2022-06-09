from django import forms

from .models import Image, Product


class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control w-100", "rows": "3"}))

    class Meta:
        model = Product
        fields = ["title", "description", "price", "category", "stock"]

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get('title')
    #     if not title.startswith('Shein'):
    #         raise forms.ValidationError('Tu producto debe empezar con Shein')
    #     return title

    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise forms.ValidationError("No puedes ingresar números negativos.")
        return price


class ImageForm(forms.ModelForm):
    image_location = forms.ImageField(required=True, label="Select an image file")

    class Meta:
        model = Image
        fields = ["image_location"]
