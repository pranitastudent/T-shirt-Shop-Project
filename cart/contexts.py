from django.shortcuts import get_object_or_404
from products.models import Product

# Code adapted from Code  Institute Mini Project Ecommerce

# Cart Contents

def cart_contents(request):
    """
    Allow items added to cart to display
    on web app
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    return {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count}
