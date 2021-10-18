import json
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import stripe


@csrf_exempt
def webhooks(request):
    """
    Listen for Stripe webhooks
    """

    stripe_secret_key = settings.STRIPE_SECRET_KEY
    payload = request.body
    event = None
    stripe.api_key = stripe_secret_key

    try:
        event = stripe.Event.construct_from(
        json.loads(payload), stripe.api_key
        )
        print('***1***')
    except ValueError as e:
        # Invalid payload
        print('***2***')
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object
        print('***3***')
        # contains a stripe.PaymentIntent
        # Then define and call a method to handle the successful payment intent.
        # handle_payment_intent_succeeded(payment_intent)
    elif event.type == 'payment_method.attached':
        payment_method = event.data.object
        print('***4***')
        # contains a stripe.PaymentMethod
        # Then define and call a method to handle the successful attachment of a PaymentMethod.
        # handle_payment_method_attached(payment_method)
    # ... handle other event types
    else:
        print('Unhandled event type {}'.format(event.type))
    print('***5***')
    return HttpResponse(status=200)
