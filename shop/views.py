from django.shortcuts import render, get_object_or_404
from .models import Product


def shop_products(request):
    """ A view to return the shop page with all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'shop/shop.html', context)


def product_detail(request, product_id):
    """ A view to return individual product and their details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)
