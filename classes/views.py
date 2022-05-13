from django.shortcuts import render

# Create your views here.


def classes(request):
    """ A view to return the classes page """

    return render(request, 'classes/classes.html')
