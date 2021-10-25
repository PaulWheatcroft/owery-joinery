from django.urls import path
from admin_tools import views

urlpatterns = [
    path('', views.get_all_orders, name='get_all_orders'),
    path('edit/<order_number>/', views.view_order_details,
         name='view_order_details'),
]
