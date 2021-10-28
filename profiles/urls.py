from django.urls import path
from profiles import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order/<order_number>/', views.view_order, name='view_order'),
]
