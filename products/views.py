from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .models import Product



# Product View- adapted from Django 3.0 documentation

def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    return render(request,"products/products.html", {"products":paged_products})


def do_search(request):
    products = Product.objects.filter(product_name__icontains=request.GET['q'])
    return render(request, "products/products.html", {"products": products})

