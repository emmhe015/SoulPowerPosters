from django.urls import path
from django.contrib.auth import views as auth_views
from .views import view_cart, add_to_cart, remove_from_cart

urlpatterns = [
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]