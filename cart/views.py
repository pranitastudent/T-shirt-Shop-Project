from django.shortcuts import get_object_or_404, redirect, render, reverse
from products.models import Product

# Create your views here.
def view_cart(request):
    cart = request.session.get('cart', {})
    sub_total = 0
    for id, quantity in cart.items():
         product = get_object_or_404(Product, pk=id)
         sub_total = sub_total + (quantity * product.price)
    """A View that renders the cart contents page"""
    return render(request, "cart/cart.html", {'sub_total':sub_total})


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})   
              
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        product = get_object_or_404(Product, pk=id)
        sub_total=0       
        sub_total = sub_total + (quantity * product.price)
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('products'), {'sub_total':sub_total})

def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    print(request.POST)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(str(id))
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))