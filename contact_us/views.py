from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ContactForm


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@xfitcrossfitbox.com'])
            except BadHeaderError:
                messages.error(request, 'Message send failed. Please ensure the form is valid.')
            return redirect('success')
    return render(request, "contact_us/contact_us.html", {'form': form})


def successView(request):
    """
    On successful message, return contact form send confirmation
    """
    return render(request, "contact_us/contact_success.html")
