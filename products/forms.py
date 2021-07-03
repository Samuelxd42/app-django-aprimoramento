from django import forms
from django.forms.widgets import URLInput
from .models import Product


class CustumerFormProducts(forms.ModelForm):
    name = forms.CharField(label='Nome')
    quantity = forms.IntegerField(label='Quantidade')
    value = forms.DecimalField(label='Valor R$')

    class Meta:
        model = Product
        fields = (
            'name', 
            'quantity', 
            'value',
        )

