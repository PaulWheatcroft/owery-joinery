import json
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

import stripe

from cart.contexts import contents_of_cart
from products.models import Product
from profiles.models import UserProfile
from .forms import OrderForm
from .models import OrderLineItems


@require_POST
def cache_checkout_data(request):
    # Put the cart and username in the meta data of the payment
    # intent so these details can be used to verify the transaction
    # Through the webhook handler
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
                'cart': json.dumps(request.session.get('cart', {})),
                'username': request.user,
            })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    # Checkout through Stripe
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        email = request.POST['email']
        # Create the form data for the database
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': email,
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'county': request.POST['county'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # If the order is valid save it but don't commit
            # as the stripe transaction details need to added
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            order_items = []
            for product_id, quantity in cart.items():
                # Iterate through the products and add them each to the
                # OrderLinesItems form
                product = Product.objects.get(id=product_id)
                order_line_items = OrderLineItems(
                    order=order,
                    product=product,
                    quantity=quantity,
                )
                order_items.append(order_line_items)
                order_line_items.save()
            if request.user.is_authenticated:
                # If the user is authenticated then
                # attach the user's profile to the order
                profile = UserProfile.objects.get(user=request.user)
                order.user_profile = profile
                order.save()

        send_mail('Confirmation Of Order', 'This is to confirm order:'
                  f'{order.order_number}',
                  settings.EMAIL_HOST_USER, [email],)

        context = {
            'order': order,
            'order_items': order_items,
        }

        cart = {}
        request.session['cart'] = cart

        return render(request, 'checkout/checkout-success.html', context)

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your shopping cart is empty")
            return redirect(reverse('products'))

        current_cart = contents_of_cart(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret
        }

        return render(request, 'checkout/checkout.html', context)
