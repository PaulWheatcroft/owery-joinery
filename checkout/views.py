from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your shopping cart is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    stripe_public_key = 'STRIPE_PUBLIC_KEY'
    client_secret = 'CLIENT_SECRET'
    context = {
       'order_form': order_form,
       'stripe_public_key': stripe_public_key,
       'client_secret': client_secret,
    }

    return render(request, 'checkout/checkout.html', context)
