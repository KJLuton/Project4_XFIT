from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about us page """

    return render(request, 'home/about.html')


def privacypolicy(request):
    """ A view to return the terms and conditions page """

    return render(request, 'home/privacypolicy.html')


def membership(request):
    """ A view to return the memberships page """

    return render(request, 'home/membership.html')


def classes(request):
    """ A view to return the classes page """

    return render(request, 'home/classes.html')
