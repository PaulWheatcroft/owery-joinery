from django.shortcuts import render, redirect, get_object_or_404
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


def edit_product(request, product_id):
    """
    A view to edit a product
    """
    edit_product_details = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = AddProductForm(
            request.POST, request.FILES, instance=edit_product_details)
        if form.is_valid():
            form.save()
        messages.success(request, 'Succesfully amended the product')
        context = {
            'form': form,
            'edit_product_details': edit_product_details,
        }

        return render(request, 'products/edit-product.html', context)

    form = AddProductForm(instance=edit_product_details)

    context = {
        'form': form,
        'edit_product_details': edit_product_details
    }

    return render(request, 'products/edit-product.html', context)


def delete_product(request, product_id):
    """
    A view to delete a product
    """
    delete_product_details = get_object_or_404(Product, id=product_id)
    category = Category.objects.get(name=delete_product_details.category)
    delete_product_details.delete()
    messages.success(request, 'Succesfully deleted the product')
    return redirect('filtered_products', category.id)
