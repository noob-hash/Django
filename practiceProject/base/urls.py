from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('register/',views.registerUser, name="register"),
    path('', views.home, name="home"),
    #name makes sure you can fetch data with its value rather than page's url
    path('product/<str:pk>/', views.product, name = "product"),
    path('category/<str:pk>/', views.category, name = "category"),
    path('addProduct/', views.addProduct, name = "addProduct"),
    path('updateProduct/<str:pk>/', views.updateProduct, name = "updateProduct"),
    path('deleteProduct/<str:pk>/', views.deleteProduct, name = "deleteProduct"),
    path('addCategory/', views.addCategory, name = "addCategory"),
    path('addReview/', views.addReview, name = "addReview"),
]