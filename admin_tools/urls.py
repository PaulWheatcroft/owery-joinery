from django.urls import path
from admin_tools import views

urlpatterns = [
    path('', views.get_orders, name='get_orders'),
    path('edit/<order_number>/', views.view_order_details,
         name='view_order_details'),
]
