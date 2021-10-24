from django.urls import path
from .views import get_all_orders, view_order_details

urlpatterns = [
    path('', get_all_orders, name='get_all_orders'),
    path('<order_number>/', view_order_details,
         name='view_order_details'),
]
