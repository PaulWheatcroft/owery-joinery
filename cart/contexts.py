from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def contents_of_cart(request):
    """ Return the cart contents to a site wide context """

    cart_items = []
    total = 0
    product_count = 0
    delivery = Decimal(10.00)
    grand_total = total + delivery
    cart = request.session.get('cart', {})

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

        grand_total = grand_total + line_total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
        'cart': cart,
    }

    return context
