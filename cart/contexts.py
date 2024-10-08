from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        if isinstance(item_data, int):
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'name': product.name,
                'price': product.price,
                'image_url': product.image_url if product.image_url else None,
            })
            total += item_data * product.price
            product_count += item_data
        else:
            quantity = item_data['quantity']
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'name': product.name,
                'price': product.price,
                'image_url': product.image_url if product.image_url else None,
            })
            total += quantity * product.price
            product_count += quantity

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
