from decimal import Decimal


def contents_of_cart(request):

    cart_items = []
    total = Decimal(0.00)
    product_count = 0
    delivery = Decimal(10.00)
    grand_total = total + delivery
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
