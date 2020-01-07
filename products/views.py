from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product


# Product View- adapted from Django 3.0 documentation

def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    return render(request, "products/products.html",
                  {"products": paged_products})


# Search - method adapted from Traversy Media - Python Django Dev To
# Development

def do_search(request):
    queryset_list = Product.objects.all()

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                product_name__icontains=keywords)

            context = {

                'products': queryset_list,
                'values': request.GET

            }
            return render(request, 'products/products.html', context)
