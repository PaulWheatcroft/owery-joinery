from django.urls import path
from .views import checkout
from .webhooks import webhook

urlpatterns = [
    path('', checkout, name='checkout'),
    path('checkout/success/', checkout, name='checkout_success'),
    path('wh/', webhook, name='webhook')
]