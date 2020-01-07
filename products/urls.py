from django.urls import path
from .views import all_products
from django.conf.urls import url
from . import views


urlpatterns = [
    path('products/', all_products, name='products'),
    path('search', views.do_search, name='search'),

]
