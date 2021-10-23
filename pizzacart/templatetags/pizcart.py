from django import template

register = template.Library()


@register.filter(name='piz_in_cart')
def piz_in_cart(item, cart):
    keys = cart.keys()
    for eid in keys:
        if int(eid) == item.eid:
            return True
    return False

@register.filter(name='item_shape')
def item_shape(item, cart):
    return item.shape


@register.filter(name='item_quantity')
def item_quantity(item, cart):
    keys = cart.keys()
    for eid in keys:
        if int(eid) == item.eid:
            return cart.get(eid)
    return 0

@register.filter(name="final_amount")
def total_amount(item, cart):
    return item.mrp * item_quantity(item, cart)


@register.filter(name="total_final_amount")
def total_final_amount(items, cart):
    sum = 0
    for i in items:
        sum += total_amount(i, cart)
    return sum