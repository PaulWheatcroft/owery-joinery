from django.shortcuts import render
from django.contrib import messages


def index(request):
    """ Load index page """
    messages.info(request, 'Testing alerts show correctly.')

    return render(request, 'home/index.html')
