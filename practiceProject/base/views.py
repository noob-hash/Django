from asyncio.windows_events import NULL
from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Category, Product, Review
from .form import CategoryForm, ProductForm, ReviewForm
# Create your views here.

def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "Incorrect username or password combination")

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Incorrect username or password combination")

    context = {'page' : page}
    return render(request, 'base/Login_Register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    page = 'register'

    context = {'page' : page}
    return render(request, 'base/Login_Register.html', context)


def home(request):
    # check if request method has something 
    # if it does return view of product with said cateogary name else show all
    query = request.GET.get('q') if request.GET.get('q') != None else ''

    #will overide above dictonary
    #variable_name = modle_name.object_attribute.method
    #method can be all, get, filter and exclude with more types of each

    # filter to filter query
    # we use __ to go query parent class
    # as shown category is parent class of product as such we use __ to query name of product
    # this method doesn't require the query to have full name
    # but only checks if the query provided is contained in categotry name
    
    # chaining filter query with or , and using Q check imports
    products = Product.objects.filter(
        Q(category__name__contains = query) |
        Q(name__contains = query)
        )
    # need to check more query methods as above contains is case insensetive
    # icontains is case sensitive, starts with checks if value starting with same letter is present


    categorys = Category.objects.all()
    reviews = Review.objects.all()
    product_count = products.count()
    # I am sending above products data as dictonary which will be called 'products'
    #something neat you can do is 
    #DataSent = {'products' : products}
    #return render(request, 'home.html', DataSent)
    context = {'categorys' : categorys, "reviews" : reviews, "products" : products, "product_count" : product_count}
    return render(request, 'base/home.html', context)

def product(request, pk):
    product = None
    product = Product.objects.get(id = pk)
    reviews = Review.objects.filter(product = pk)
    context = {'product' : product, 'reviews' : reviews}
    return render(request, 'base/product.html', context)

def category(request, pk):
    category = None
    category = Category.objects.get(id = pk)
    products = Product.objects.all()
    context = {'category' : category, 'products' : products}
    return render(request, 'base/category.html', context)

# without loging in user can only view
#  not perform any action
@login_required(login_url="login")
def addProduct(request):
    form = ProductForm()

    #check for post method in form, post is sumbit
    if request.method == 'POST':
        #get form value according to model of form i.e product
        form = ProductForm(request.POST)
        #check if form has valid input 
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'base/Product_form.html', context)

@login_required(login_url="login")
def addReview(request):
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'base/Review_form.html', context)

@login_required(login_url="login")
def updateProduct(request, pk):
    #get product by id pk
    product = Product.objects.get(id = pk)
    #fill form with data from product
    form = ProductForm(instance = product)

    if request.user != product.user:
        return HttpResponse('You are not owner of this product!!')

    if request.method == 'POST':
        #change form data to new data
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'base/Product_form.html', context)

@login_required(login_url="login")
def deleteProduct(request, pk):
    product = Product.objects.get(id = pk)

    if request.user != product.user:
        return HttpResponse('You are not owner of this product!!')
    
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    context = {'obj' : product}
    return render(request, 'base/delete.html', context)

@login_required(login_url="login")
def addCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'base/Category_form.html', context)

@login_required(login_url="login")
def updateCategory(request, pk):
    category = Category.objects.get(id = pk)
    form = CategoryForm(instance=pk)

    if request.user != category.user:
        return HttpResponse('You are not owner of this product!!')

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'base/Category_form.html', context)