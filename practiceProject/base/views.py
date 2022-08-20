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
    #something neat you can do is 
    #DataSent = {'products' : products}
    #return render(request, 'home.html', DataSent)
    return render(request, 'base/home.html', {'products' : products})

def product(request, pk):
    product = None
    for i in products:
        if i['id'] == int(pk):
            product = i
    context = {'product' : product}
    return render(request, 'base/product.html', context)
