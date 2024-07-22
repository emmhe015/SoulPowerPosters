from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm

def home(request):
    return render(request, 'store/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'store/register.html', {'form': form})


