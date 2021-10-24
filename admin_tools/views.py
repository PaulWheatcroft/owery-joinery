from django.shortcuts import render, get_object_or_404
from checkout.models import Order, OrderLineItems, OrderStatus
from .forms import OrderStatusForm


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
    A view to return an order's details
    """
    order = Order.objects.filter(order_number=order_number)
    line_items = OrderLineItems.objects.filter(order=order[0].id)
    order_status_form = OrderStatusForm(instance=order[0].status)

    context = {
        'order': order,
        'line_items': line_items,
        'order_status_form': order_status_form,
    }

    return render(request, 'admin_tools/view_order_details.html', context)


def update_order_status(request, order_number):
    """
    A view to update an order's status
    """
    if request.method == 'POST':
        order = Order.objects.filter(order_number=order_number)
        new_status = request.POST.get('status_name')
        status = OrderStatus.objects.filter(status_name=new_status)
        line_items = OrderLineItems.objects.filter(order=order[0].id)
        order.update(status=status[0].id)
        order_status_form = OrderStatusForm
        context = {
            'order': order,
            'line_items': line_items,
            'order_status_form': order_status_form,
        }
        print(order_number)
        print(order)
        return render(request, 'admin_tools/view_order_details.html', context)
