from django.urls import path
from .views import checkout

urlpatterns = [
    path('', checkout, name='checkout'),
    path('checkout/success/', checkout, name='checkout_success'),
]