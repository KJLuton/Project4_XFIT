from django.shortcuts import render
from .models import Product


def shop_products(request):
    """ A view to return the shop page with all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'shop/shop.html', context)
