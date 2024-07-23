from django.shortcuts import render, get_object_or_404, redirect
from .cart import *
from products.models import Product
from .forms import AddProductToCartForm
from django.contrib import messages
from django.utils.translation import gettext as _

# with initial we can assign a value to the attribiutes of a form.
def cart_view(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = AddProductToCartForm(
            initial={
                'quantity': item['quantity'],
                'replace_quantity': True
            }
        )


    return render(request, 'cart/cart.html', {'cart': cart})


def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddProductToCartForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity, replace_quantity=cleaned_data['replace_quantity'])
        messages.success(request, _('Product was successfully added to Shopping Cart.'))
    else:
        messages.error(request, _('There was a Problem.'))
    return redirect("cart:cart_view")


def delete_product_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.delete(product)
    messages.success(request, _('Product was successfully deleted from the Shopping Cart.'))
    return redirect("cart:cart_view")


def clear_cart(request):
    cart = Cart(request)
    if len(cart):
        cart.clear()
        messages.success(request, _('All Products were successfully removed.'))
        return redirect('cart:cart_view')
    else:
        messages.error(request, _('Your cart is already empty!'))
        return redirect('cart:cart_view')
