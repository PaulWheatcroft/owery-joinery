from django.shortcuts import render
from django.contrib import messages
from products.models import Category


def index(request):
    """ A view to return the index page """
    messages.info(request, 'Testing alerts show correctly.')

    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'home/index.html', context)
