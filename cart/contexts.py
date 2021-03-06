from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings
from products.models import Product


def contents_of_cart(request):
    """ Return the cart contents to a site wide context """

    cart_items = []
    total = 0
    product_count = 0
    delivery = Decimal(settings.DELIVERY_COST)
    grand_total = total + delivery
    cart = request.session.get('cart', {})
    total_number_of_items = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        line_total = quantity * product.price
        cart_items.append({
            'product': product,
            'product_id': product_id,
            'quantity': quantity,
            'price': product.price,
            'line_total': line_total,
        })
        total_number_of_items += quantity
        grand_total = grand_total + line_total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
        'cart': cart,
        'total_number_of_items': total_number_of_items
    }

    return context
