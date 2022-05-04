from decimal import Decimal
from django.conf import settings

def checkout_contents(request):

    checkout_items = []
    total = 0
    product_count = 0

    context = {
        'checkout_items': checkout_items,
        'total': total,
        'product_count': product_count,
    }

    return context
