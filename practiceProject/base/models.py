from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#creating database instance
#instance's first word is capatilized best practice

class Product(models.Model):
    #user needs to be added
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    #columns and it's data type ant other values for database
    name = models.CharField(max_length=200)

    #first for database, second for form to let empty value allowed
    productDescription = models.TextField(null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    price = models.IntegerField(null = True)

    #diff between auto_now and auto_now_add is
    #auto_now updates every time this instance is used
    #auto_now_add update once it is created and that's it

    #to make new and updated data come first, prioritize update then created
    #- means data in decending with new value first
    #Meta class means it has something of importance
    class Meta:
        ordering = ['-updatedDate', 'createdDate']

    #return when called aka methods
    def __str__(self):
        return self.name

class Review(models.Model):
    #user needs to be added
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null = True)
    star = models.IntegerField(default = 0)
    comment = models.TextField(null = True, blank = True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def _str_(self):
        return {'star' : self.star, 'comment': self.comment[0:50]}