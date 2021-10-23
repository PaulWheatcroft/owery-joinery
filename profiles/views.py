from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile

from checkout.models import Order


def profile(request):
    """ A view to return the logged in user's profile page """
    if request.user.is_authenticated:
        logged_in_profile = get_object_or_404(UserProfile, user=request.user)
        print(logged_in_profile)

        orders = Order.objects.filter(user_profile=logged_in_profile)
        print(orders)

        return render(request, 'profiles/profile.html')
    else:
        return redirect('account_signup') 
