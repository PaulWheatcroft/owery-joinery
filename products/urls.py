from django.urls import path
from .views import all_products, filtered_products

urlpatterns = [
    path('', all_products, name='products'),
    path('<category_id>', filtered_products, name='filtered_products'),
]
