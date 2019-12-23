from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .models import Product

# Product View

def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    return render(request,"products/products.html", {"products":paged_products})
