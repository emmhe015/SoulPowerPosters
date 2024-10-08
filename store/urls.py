from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, register, login_view

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='store/logout.html'), name='logout'),
  

]