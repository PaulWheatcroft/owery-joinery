from django.shortcuts import render
from products.models import Category


def user_profile(request):
    """ A view to return the index page """

    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'profiles/profile.html', context)
