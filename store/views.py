from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from .models import Product, Cart, CartItem


def home(request):
    products = Product.objects.all() 
    return render(request, 'store/home.html/', {'products': products})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'store/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'store/dashboard.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'store/profile.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.name} was added to your cart.")
    return redirect('product_detail', product_id=product.id)

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.get_total_item_price() for item in items)

    return render(request, 'store/cart.html', {'items': items, 'total_price': total_price})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()

    messages.success(request, "Item was removed from your cart.")
    return redirect('view_cart')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})


