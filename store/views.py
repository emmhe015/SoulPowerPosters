from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from products.models import Product


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








