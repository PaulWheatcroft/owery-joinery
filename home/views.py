from django.shortcuts import render
from products.models import Category


def error_404_view(request, exception):
    """ A view to return a 404 page when debug is false """
    return render(request, '404.html')


def index(request):
    """ A view to return the index page """

    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'home/index.html', context)


def about(request):
    """ A view to return the about page """

    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'home/about.html', context)


def contact(request):
    """ A view to return the about page """

    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'home/contact.html', context)
