from django import forms
from .models import UserProduct, Product


class UserProductForm(forms.ModelForm):
    class Meta:
        model = UserProduct
        fields = ['price', 'quantity', 'want']