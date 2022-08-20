from django.shortcuts import render
# Create your views here.

products = [
    {'id' : 1, 'name' : 'Airsoft Gun'},
    {'id' : 2, 'name' : 'Scope'},
    {'id' : 3, 'name' : 'Mag safe'},
    {'id' : 4, 'name' : 'Helmet'},
]

def home(request):
    # I am sending above products data as dictonary which will be called 'products'
    return render(request, 'home.html', {'products' : products})

def product(request):
    return render(request, 'product.html')
