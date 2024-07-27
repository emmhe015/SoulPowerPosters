from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import Cart, CartItem
from products.models import Product

def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
    context = {
        'cart': cart,
        'total_price': total_price,
    }
    return render(request, 'cart/cart.html', context)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': 1,
            'image_url': product.image.url if product.image else '',
        }
    
   
    request.session['cart'] = cart
    
    return redirect('view_cart')

def update_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        quantity = int(request.POST.get('quantity', 1))
        if str(product_id) in cart:
            if quantity > 0:
                cart[str(product_id)]['quantity'] = quantity
            else:
                del cart[str(product_id)]
    return redirect('cart:view_cart')

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['cart'] = cart
    messages.success(request, "Item was removed from your cart.")
    return redirect('view_cart')