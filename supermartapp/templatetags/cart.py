from django import template

register = template.Library()


@register.filter(name="is_in_cart")
def is_in_cart(product, cart):
    res = not bool(cart)
    if res != True:
        keys = cart.keys()
        for id in keys:
            if int(id) == product.id:
                return "Quantity: "
        return ''
    else:
        return ''


@register.filter(name="cart_quantity")
def cart_quantity(product, cart):
    res = not bool(cart)
    if res != True:
        keys = cart.keys()
        for id in keys:
            if int(id) == product.id:
                return cart.get(id)
        return 0


@register.filter(name="product_total")
def product_total(product, cart):
    return product.price * cart_quantity(product, cart)


@register.filter(name="total_cart_price")
def total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum += product_total(p, cart)

    return sum
