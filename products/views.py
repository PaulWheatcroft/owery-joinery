from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Style
from .forms import AddProductForm


def all_products(request):
    """ A view to return all products """

    products = Product.objects.all().order_by('category')
    styles = Style.objects.all()
    selected_category = '0'
    selected_style = '0'
    sort = '1'

    if request.method == 'POST':
        selected_category = request.POST.get('filter-category')
        selected_style = request.POST.get('filter-style')
        sort = request.POST.get('sort-radio')

        if sort == '1':
            selected_sort = int(sort)
            if selected_category > '0' and selected_style > '0':
                products = Product.objects.filter(
                    category=selected_category,
                    style=selected_style).order_by('price')
            elif selected_category > '0' and selected_style == '0':
                products = Product.objects.filter(
                    category=selected_category).order_by('price')
            elif selected_category == '0' and selected_style > '0':
                products = Product.objects.filter(
                    style=selected_style).order_by('price')
            else:
                products = Product.objects.all().order_by('price')
        else:
            selected_sort = int(sort)
            if selected_category > '0' and selected_style > '0':
                products = Product.objects.filter(
                    category=selected_category,
                    style=selected_style).order_by('-price')
            elif selected_category > '0' and selected_style == '0':
                products = Product.objects.filter(
                    category=selected_category).order_by('-price')
            elif selected_category == '0' and selected_style > '0':
                products = Product.objects.filter(
                    style=selected_style).order_by('-price')
            else:
                products = Product.objects.all().order_by('-price')

        context = {
            'products': products,
            'styles': styles,
            'selected_category': selected_category,
            'selected_style': selected_style,
            'sort': selected_sort
        }

        return render(request, 'products/products.html', context)

    context = {
        'products': products,
        'styles': styles,
        'selected_category': selected_category,
        'selected_style': selected_style,
        'sort': sort
    }

    return render(request, 'products/products.html', context)


def filtered_products(request, category_id):
    """ A view to return products filtered by category """

    products = Product.objects.filter(category_id=category_id)
    styles = Style.objects.all()
    selected_category = category_id
    category = Category.objects.get(id=category_id)
    selected_style = '0'
    sort = '1'

    context = {
        'products': products,
        'styles': styles,
        'selected_category': selected_category,
        'selected_style': selected_style,
        'sort': sort,
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


@login_required
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


@login_required
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


@login_required
def delete_product(request, product_id):
    """
    A view to delete a product
    """
    delete_product_details = get_object_or_404(Product, id=product_id)
    category = Category.objects.get(name=delete_product_details.category)
    delete_product_details.delete()
    messages.success(request, 'Succesfully deleted the product')
    return redirect('filtered_products', category.id)
