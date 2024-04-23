from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image']  # 仅包括图片字段，或者包括你想要展示的所有字段
