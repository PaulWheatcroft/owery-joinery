from django.http import HttpResponse
from .webhooks import webhook


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
        return HttpResponse(
            content=f'Successful webhook received: {event["type"]}',
            status=200)


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle standard response for unsuccessful webhook event
        """
        return HttpResponse(
            content=f'Failed webhook received: {event["type"]}',
            status=200)