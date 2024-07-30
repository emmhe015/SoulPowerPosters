from django.urls import path
from .views import product_list, product_detail, all_products, add_product, edit_product, delete_product

app_name = 'products'

urlpatterns = [
    path('', all_products, name='products'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('add/', add_product, name='add_product'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('delete/<int:product_id>/',
         delete_product,
         name='delete_product'),
]