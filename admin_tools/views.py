from django.shortcuts import render
from checkout.models import Order, OrderLineItems
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import OrderStatusForm


@login_required
def get_all_orders(request):
    """
    A view to return the list of all orders
    """
    all_orders = Order.objects.all().order_by('date').reverse()

    if request.method == 'POST':
        text = request.POST.get('search-order-text')
        searched_orders = Order.objects.filter(
            Q(first_name__icontains=text)
            | Q(last_name__icontains=text))
        all_orders = searched_orders

        context = {
            'all_orders': all_orders,
        }
        return render(request, 'admin_tools/orders.html', context)

    context = {
        'all_orders': all_orders,
    }
    return render(request, 'admin_tools/orders.html', context)


@login_required
def view_order_details(request, order_number):
    """
    A view to return an order's details
    """
    order = Order.objects.filter(order_number=order_number)
    line_items = OrderLineItems.objects.filter(order=order[0].id)
    order_status_form = OrderStatusForm(instance=order[0].status)

    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order[0])
        form.status = order[0].status
        if form.is_valid():
            form.save()
        messages.success(request, 'Succesfully amended the status')
        order_status_form = form

        context = {
            'order': order,
            'line_items': line_items,
            'order_status_form': order_status_form,
        }
        return render(request, 'admin_tools/view_order_details.html', context)

    context = {
        'order': order,
        'line_items': line_items,
        'order_status_form': order_status_form,
    }

    return render(request, 'admin_tools/view_order_details.html', context)
