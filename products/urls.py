from django.urls import path
from products import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<product_id>', views.edit_product, name='edit_product'),
    path('delete/<product_id>', views.delete_product, name='delete_product'),
    path('<category_id>/', views.filtered_products, name='filtered_products'),
    path('product/<product_id>/',
         views.product_details, name='product_details'),
]
