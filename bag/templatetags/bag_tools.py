from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculate the subtotal of the products in the bag when
    multiple items/sizes of the same item are in the bag.
    """
    return price * quantity
