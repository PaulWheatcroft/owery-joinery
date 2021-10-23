from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def profile(request):
    """ A view to return the logged in user's profile page """
    profile = get_object_or_404(UserProfile, user=request.user)
    print(profile)

    orders = profile.orders.all()

    print(orders)

    return render(request, 'profiles/profile.html')
