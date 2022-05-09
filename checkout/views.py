from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('shop'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KxYpSCM2Ai73xrSdur7lZWWItkEbA3ltAq6JkjWxBuqQ3RlYMxZxSnTWjNQNNkAl609E3dgZP0qXxS4aDcDW43M00bQ4R3luw',
        'client_secret': 'text client secret',
    }

    return render(request, template, context)
