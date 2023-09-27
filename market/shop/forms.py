from django import forms
from .models import UserProduct, Product


class UserProductForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        empty_label='товар',
        widget=forms.Select({'class': 'form-control'}),
    )

    class Meta:
        model = UserProduct
        fields = ['price', 'quantity', 'want']
        # widgets = {
        #     'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
        #     'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество'}),
        # }
