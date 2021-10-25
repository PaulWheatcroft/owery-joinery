from django.urls import path
from .views import all_products, filtered_products, product_details, add_product, edit_product

urlpatterns = [
    path('', all_products, name='products'),
    path('add/', add_product, name='add_product'),
    path('edit/<product_id>', edit_product, name='edit_product'),
    path('<category_id>/', filtered_products, name='filtered_products'),
    path('product/<product_id>/', product_details, name='product_details'),
]
