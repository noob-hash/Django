from dataclasses import fields
from django.forms import ModelForm
from .models import Category, Product, Review

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'