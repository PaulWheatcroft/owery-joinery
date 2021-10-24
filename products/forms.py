from django import forms
from .models import Product


class AddProductForm(forms.ModelForm):
    """
    Allow a staff member to add a new product
    """
    class Meta:
        model = Product
        fields = ('category', 'style', 'name',
                  'sku', 'description',
                  'price', 'height', 'width', 'image')
