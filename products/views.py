from django.shortcuts import render
from .models import Product


# Create your views here.


def all_products(request):
    """ A view to return all products """

    products = Product.objects.all()

    print('all and all')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def filtered_products(request, category_id):
    """ A view to return products filtered by category """

    products = Product.objects.filter(category=category_id)

    print('filtered')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
