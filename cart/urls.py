from django.urls import path
from cart import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add_product/<product_id>/', views.add_to_cart, name='add_to_cart'),
    path('amend/<product_id>/', views.amend_cart, name='amend_cart'),
    path('remove/<product_id>/', views.remove_product_from_cart, name='remove_product_from_cart'),
]
