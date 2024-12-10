from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'id' : 'Product ID',
            'name' : 'Product Name',
            'sku' : 'Product SKU',
            'price' : 'Product Price',
            'quantity' : 'Product Quantity',
            'supplier' : 'Product Supplier',
        }
        widgets = {
            'id' : forms.NumberInput(attrs={
                'placeholder': 'e.g. 1',
                'class': 'form-control',
            }),

            'name' : forms.TextInput(attrs={
                'placeholder': 'e.g. Shirt',
                'class': 'form-control',
            }),

            'sku' : forms.TextInput(attrs={
                'placeholder': 'e.g. A1234',
                'class': 'form-control',
            }),

            'price' : forms.NumberInput(attrs={
                'placeholder': 'e.g. 1.00',
                'class': 'form-control',
            }),

            'quantity' : forms.NumberInput(attrs={
                'placeholder': 'e.g. 10',
                'class': 'form-control',
            }),

            'supplier' : forms.TextInput(attrs={
                'placeholder': 'e.g. Abc',
                'class': 'form-control',
            })
        }