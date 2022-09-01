from django.shortcuts import render
from .models import Products
# Create your views here.



def home(request):
    #will overide above dictonary
    #variable_name = modle_name.object_attribute.method
    #method can be all, get, filter and exclude with more types of each
    products = Products.objects.all()
    # I am sending above products data as dictonary which will be called 'products'
    #something neat you can do is 
    #DataSent = {'products' : products}
    #return render(request, 'home.html', DataSent)
    return render(request, 'base/home.html', {'products' : products})

def product(request, pk):
    product = None
    product = Products.objects.get(id = pk)
    context = {'product' : product}
    return render(request, 'base/product.html', context)
