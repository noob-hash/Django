from django.db import models

# Create your models here.

#creating database instance
#instance's first word is capatilized best practice

class Product(models.Model):
    #columns and it's data type ant other values for database
    name = models.CharField(max_length=200)

    #first for database, second for form to let empty value allowed
    productDescription = models.TextField(null=True, blank=True)
    firstPlaced = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=True)

    #diff between auto_now and auto_now_add is
    #auto_now updates every time this instance is used
    #auto_now_add update once it is created and that's it

    