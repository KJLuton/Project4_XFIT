from django.shortcuts import render


def profile(request):
    """ display he users profile """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
