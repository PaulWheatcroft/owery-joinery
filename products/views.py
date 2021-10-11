from django.shortcuts import render
from .models import Product


# Create your views here.


def all_products(request):
    """ A view to return all products """

    all_avilable_products = Product.objects.all()

    products = all_avilable_products.order_by('category')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def filtered_products(request, category_id):
    """ A view to return products filtered by category """

    products_in_a_category = Product.objects.filter(category=category_id)

    products = products_in_a_category.order_by('style')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
