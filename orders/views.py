from django.shortcuts import render, redirect
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import OrderItem
from django.contrib import messages
from django.utils.translation import gettext as _


@login_required
def order_view(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, _('You can not proceed to Checkout page because your Shopping cart is empty'))
        return redirect('products_list')
    if request.method == 'POST':

        order = OrderForm(request.POST)
        if order.is_valid():  # if the request was post we validate the form order without committing so that we can
            order_obj = order.save(commit=False)
            order_obj.user = request.user  # set the user of order
            order_obj.save()  # after creating the order we need to create the order items based on cart to the database
            for item in cart:  # so we first create an object from cart, and then we loop over it and for each item in
                product = item['product_obj']  # cart we get the real product that we saved as ['product_obj'] dict
                OrderItem.objects.create(  # on cart and create an order item based on that and other information from
                    order=order_obj,  # cart,and we set the order that we just created(order_obj) as order of order item
                    product=product,  # with this loop we create an order item for each product in our cart.
                    quantity=item['quantity'],  # after that we need to clear the cart.
                    price=product.price,
                )
            cart.clear()
            request.session['order_id'] = order_obj.id
            messages.success(request, 'Your Order has successfully placed.')
            return redirect('payment:process')

    return render(request, 'orders/checkout.html', context={
        'form': OrderForm(),
    })


