from django.shortcuts import render
from products.models import Product

# Code taken from Code Institute.
def search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
    