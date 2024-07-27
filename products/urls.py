from django.urls import path
from .views import product_list, product_detail, all_products

app_name = 'products'

urlpatterns = [
    path('', all_products, name='products'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
]