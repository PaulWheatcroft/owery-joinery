from django.http import HttpResponse
from .models import Order
from products.models import Product
from .models import OrderLineItems

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle generic response from webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle standard response for successful webhook event
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        name = billing_details.name
        first_name = name.split(' ', 1)[0]
        last_name = name.split(' ', 1)[1]
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount/100, 2)

        # If the shipping address is empty set to none
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.adress[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    stripe_pid=pid,
                    )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'webhook received: {event["type"]} | SUCCESS\
                    : Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    town_or_city=billing_details.address.city,
                    postcode=billing_details.address.postal_code,
                    county=billing_details.address.state,
                    country=billing_details.address.country,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order.save()
                order_items = []
                for product_id, quantity in json.loads(cart).items():

                    product = Product.objects.get(id=product_id)
                    order_line_items = OrderLineItems(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_items.append(order_line_items)
                    order_line_items.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'webhook received: {event["type"]} | Error: {e}',
                    status=500)

        # Remove print before submitting
        print(intent)
        return HttpResponse(
            content=f'webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle standard response for unsuccessful webhook event
        """
        return HttpResponse(
            content=f'webhook received: {event["type"]}',
            status=200)
