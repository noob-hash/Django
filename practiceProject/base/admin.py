from django.contrib import admin

# Register your models here.

from .models import Products, Review

#add into database in app

admin.site.register(Products)
admin.site.register(Review)