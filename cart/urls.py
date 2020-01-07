from django.contrib import admin
from django.urls import path
from .views import view_cart, add_to_cart, adjust_cart


urlpatterns = [
    path('view_cart/', view_cart, name="view_cart"),
    path('<int:id>/add_to_cart/', add_to_cart, name="add_to_cart"),
    path('<int:id>/adjust_cart/', adjust_cart, name="adjust_cart")
]
