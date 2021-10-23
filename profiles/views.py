from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile

from checkout.models import Order, OrderLineItems


def profile(request):
    """
    A view to return the logged in user's profile page
    which contains a list of their previous orders
    """
    if request.user.is_authenticated:
        logged_in_profile = get_object_or_404(UserProfile, user=request.user)

        orders = Order.objects.filter(user_profile=logged_in_profile)

        context = {
            'logged_in_profile': logged_in_profile,
            'orders': orders,
        }

        return render(request, 'profiles/profile.html', context)
    else:
        return redirect('account_signup')


def view_order(request, order_number):
    """
    A view to return an order;s details
    """
    order = Order.objects.filter(order_number=order_number)
    line_items = OrderLineItems.objects.filter(order=order[0].id)

    context = {
        'order': order,
        'line_items': line_items
    }

    return render(request, 'profiles/order_details.html', context)
