from django.urls import path
from .views import view_cart, add_to_cart

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<product_id>', add_to_cart, name='add_to_cart'),
]
