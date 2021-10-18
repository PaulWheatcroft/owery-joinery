from django.http import HttpResponse
from .webhooks import webhooks


class StripeWebhookHandler:
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

    def payment_successful(self, event):
        """
        Handle standard response for successful webhook event
        """
        return HttpResponse(
            content=f'Successful webhook received: {event["type"]}',
            status=200)


    def payment_failed(self, event):
        """
        Handle standard response for successful webhook event
        """
        return HttpResponse(
            content=f'Failed webhook received: {event["type"]}',
            status=200)