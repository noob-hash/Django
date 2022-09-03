from django.shortcuts import redirect,render
from .models import Product
from .form import ProductForm
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
    return render(request, 'base/addProduct.html', context)