from django.urls import path
from .views import view_cart, add_to_cart, amend_cart, remove_product_from_cart

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add_product/<product_id>/', add_to_cart, name='add_to_cart'),
    path('amend/<product_id>/', amend_cart, name='amend_cart'),
    path('remove/<product_id>/', remove_product_from_cart, name='remove_product_from_cart'),
]
