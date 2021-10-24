from django.shortcuts import render
from checkout.models import Order, OrderLineItems


def get_all_orders(request):
    """
    A view to return the logged in user's profile page
    which contains a list of their previous orders
    """
    all_orders = Order.objects.all()

    context = {
        'all_orders': all_orders,
    }
    return render(request, 'admin_tools/orders.html', context)


def view_order_details(request, order_number):
    """
    A view to return an order;s details
    """
    order = Order.objects.filter(order_number=order_number)
    line_items = OrderLineItems.objects.filter(order=order[0].id)

    context = {
        'order': order,
        'line_items': line_items
    }

    return render(request, 'admin_tools/view_order_details.html', context)
