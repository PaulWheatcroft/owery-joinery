from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from checkout.models import Order, OrderLineItems, OrderStatus
from .forms import OrderStatusForm


@login_required
def get_orders(request):
    """
    A view to return the list of all orders
    """
    all_orders = Order.objects.all().order_by('date').reverse()
    all_status = OrderStatus.objects.all().order_by('status_id')
    selected_status = '0'

    if request.method == 'POST':
        text = request.POST.get('search-order-text')
        status = request.POST.get('search-status')
        selected_status = status

        if text == '' and status == '0':
            orders = all_orders
        elif status == '0':
            searched_orders = Order.objects.filter(
                Q(first_name__icontains=text)
                | Q(last_name__icontains=text))
            orders = searched_orders
        else:
            searched_orders = Order.objects.filter(
                Q(first_name__icontains=text, status=status)
                | Q(last_name__icontains=text, status=status))
            orders = searched_orders

        context = {
            'orders': orders,
            'all_status': all_status,
            'selected_text': text,
            'selected_status': selected_status,
        }
        return render(request, 'admin_tools/orders.html', context)

    context = {
        'orders': all_orders,
        'all_status': all_status,
        'selected_status': selected_status,
    }
    return render(request, 'admin_tools/orders.html', context)


@login_required
def view_order_details(request, order_number):
    """
    A view to return an order's details
    """
    order = Order.objects.filter(order_number=order_number)
    line_items = OrderLineItems.objects.filter(order=order[0].id)
    order_status_form = OrderStatusForm(instance=order[0])

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
