from django.contrib import admin

# Register your models here.

from .models import Product

#add into database in app

admin.site.register(Product)