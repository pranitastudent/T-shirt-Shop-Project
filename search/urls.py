from django.conf.urls import url
from .views import search
from django.urls import path

urlpatterns = [
    path('search/', search, name='search'),  
]
