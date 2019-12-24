from django.urls import path
from .views import all_products
from django.conf.urls import url

urlpatterns = [
    path('products/', all_products, name='products'),  
 
    
]