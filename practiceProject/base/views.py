from asyncio.windows_events import NULL
from unicodedata import category
from django.shortcuts import redirect,render
from .models import Category, Product
from .form import CategoryForm, ProductForm
# Create your views here.



def home(request):
    #will overide above dictonary
    #variable_name = modle_name.object_attribute.method
    #method can be all, get, filter and exclude with more types of each
    products = Product.objects.all()
    # I am sending above products data as dictonary which will be called 'products'
    #something neat you can do is 
    #DataSent = {'products' : products}
    #return render(request, 'home.html', DataSent)
    return render(request, 'base/home.html', {'products' : products})

def product(request, pk):
    product = None
    product = Product.objects.get(id = pk)
    context = {'product' : product}
    return render(request, 'base/product.html', context)

def addProduct(request):
    form = ProductForm()

    #check for post method in form, post is sumbit
    if request.method == 'POST':
        #get form value according to model of form i.r product
        form = ProductForm(request.POST)
        #check if form has valid input 
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'base/Product_form.html', context)

def updateProduct(request, pk):
    #get product by id pk
    product = Product.objects.get(id = pk)
    #fill form with data from product
    form = ProductForm(instance = product)
    if request.method == 'POST':
        #change form data to new data
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'base/Product_form.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id = pk)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    context = {'obj' : product}
    return render(request, 'base/delete.html', context)

def addCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'base/Category_form.html', context)

def updateCategory(request, pk):
    category = Category.objects.get(id = pk)
    form = CategoryForm(instance=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'base/Category_form.html', context)