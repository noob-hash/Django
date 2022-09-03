from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #name makes sure you can fetch data with its value rather than page's url
    path('product/<str:pk>/', views.product, name = "product"),
    path('addProduct/', views.addProduct, name = "addProduct"),
    path('updateProduct/<str:pk>/', views.updateProduct, name = "updateProduct"),
    path('deleteProduct/<str:pk>/', views.deleteProduct, name = "deleteProduct"),
]