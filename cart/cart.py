from products.models import Product


class Cart:
    def __init__(self, request):
        self.request = request  # initialize the request(save it to self  as request)
        self.session = request.session  # initialize the session of the request(save it to self  as session)
        cart = self.session.get('cart')  # if the user already has a card we save it to self as 'cart' variable but if
        if not cart:  # the user is having a card for the first time we create a session for it and then save it to
            # 'cart' variable
            self.session['cart'] = {}  # make an empty session for ['cart'] that will be filled by the cart of the user
            cart = self.session['cart']
        self.cart = cart

    def add(self, product, quantity, replace_quantity=False):
        product_id = str(product.id)  # what product want to be added to cart
        if product_id not in self.cart:  # if it isn't already in cart specify a quantity of 0 to that product_id
            self.cart[product_id] = {'quantity': 0}
        if replace_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:  # but if it already exists add the wanted quantity to the quantity of that product_id
            self.cart[product_id]['quantity'] += quantity

        self.save()  # and at last we save the changes to the cart

    def delete(self, product):
        product_id = str(product.id)
        if product_id in self.cart:  # if the product that we want to remove exists in the cart we remove it and make
            del self.cart[product_id]
            self.save()  # the changes to the cart

# inorder to loop over the products in a cart we need the __iter__ method because it's an object.in order to loop in the
# real products in database we need to add it to cart. inorder to do that we first need to get that from database with
#  the product_id saved in cart. we get the product_ids by '.key()' method and save it into a variable and then pass it
# to our lookup statement 'id__in' . with that we take the products with saved id in carts from the database.second
# we need a copy of the cart and then add the real products to the copy of it so that we don't change the cart.to add
# real products to the copy_version of the cart we need to first loop over fetched_products and specify a key and put
# the real product as the value of the key for every fetched_products.at the end we loop over cart.values to get every
# full object of product with its id and quantity

    def __iter__(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product_obj'] = product
        for item in cart.values():
            item['product_total_price'] = item['quantity'] * item['product_obj'].price
            yield item

# method to know the number of products in cart
    def __len__(self):
        return len(self.cart.keys())

# method to clear the cart
    def clear(self):
        del self.session['cart']
        self.save()

# method to get the total price to purchase the cart
    def get_cart_total_price(self):
        cart_total_price = sum(item['quantity'] * item['product_obj'].price for item in self.cart.values())
        return cart_total_price

    def save(self):
        self.session.modified = True
