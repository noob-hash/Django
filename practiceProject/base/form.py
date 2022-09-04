from dataclasses import fields
from django.forms import ModelForm
from .models import Categories, Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'