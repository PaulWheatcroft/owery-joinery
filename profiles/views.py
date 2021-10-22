from django.shortcuts import render


def profile(request):
    """ A view to return the logged in user's profile page """

    return render(request, 'profiles/profile.html')
