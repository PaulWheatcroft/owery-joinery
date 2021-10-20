from django.urls import path
from .views import checkout, cache_checkout_data
from .webhooks import webhook

urlpatterns = [
    path('', checkout, name='checkout'),
    path('success/', checkout, name='checkout_success'),
    path('cache_checkout_data/', cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook')
]
