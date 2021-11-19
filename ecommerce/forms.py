from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    
    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get('title')
    #     if not title.startswith('Shein'):
    #         raise forms.ValidationError('Tu producto debe empezar con Shein')
    #     return title
    
    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError('No puedes ingresar números negativos.')
        return price