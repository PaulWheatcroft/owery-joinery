from django.shortcuts import render, get_object_or_404
from products.models import Category

from .models import AdditionalUserDetails


def profile(request):
    """ A view to return the logged in user's profile page """

    categories = Category.objects.all()
    additional_details = AdditionalUserDetails()

    context = {
        'categories': categories,
        'additional_details': additional_details,
    }

    return render(request, 'profiles/profile.html', context)
