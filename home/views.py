from django.shortcuts import render
from django.contrib import messages


def index(request):
    messages.success(request, 'Something went wrong!.')

    """ A view to return the index page """
    return render(request, 'home/index.html')
