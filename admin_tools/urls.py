from django.urls import path
from .views import get_all_orders, view_order_details, update_order_status

urlpatterns = [
    path('', get_all_orders, name='get_all_orders'),
    path('<order_number>/', view_order_details,
         name='view_order_details'),
    path('status-update/<order_number>/', update_order_status,
         name='update_order_status'),
]
