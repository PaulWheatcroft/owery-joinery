from django.urls import path
from .views import profile, view_order

urlpatterns = [
    path('', profile, name='profile'),
    path('order/<order_number>/', view_order, name='view_order'),
]
