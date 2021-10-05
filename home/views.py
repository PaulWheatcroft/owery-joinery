from django.shortcuts import render
from django.contrib import messages


def index(request):
    """ Load index page """
    messages.success(request, 'Something went wrong!.')

    return render(request, 'home/index.html')
