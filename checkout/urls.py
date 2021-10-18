from django.urls import path
from .views import checkout
from .webhooks import webhooks

urlpatterns = [
    path('', checkout, name='checkout'),
    path('checkout/success/', checkout, name='checkout_success'),
    path('webhooks/', webhooks, name='webhooks')
]