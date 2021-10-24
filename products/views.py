from django.shortcuts import render
from django.contrib import messages
from .models import Product, Category
from .forms import AddProductForm


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
    category = Category.objects.get(id=category_id)

    products = products_in_a_category.order_by('style')

    context = {
        'products': products,
        'category': category,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to return product details """

    product = Product.objects.get(id=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product-details.html', context)


def add_product(request):
    """
    A view to add a product
    """
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, 'Succesfully added a new product')
        form = AddProductForm()

        context = {
            'form': form,
        }

        return render(request, 'products/add-product.html', context)
    form = AddProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/add-product.html', context)
