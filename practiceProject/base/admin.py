from unicodedata import category
from django.contrib import admin

# Register your models here.

from .models import Category, Product, Review

#add into database in app

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Category)