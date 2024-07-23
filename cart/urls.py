from django.urls import path, include
from .views import cart_view, add_to_cart, delete_product_from_cart, clear_cart

app_name = 'cart'

urlpatterns = [
    path('', cart_view, name='cart_view'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('delete/<int:product_id>/', delete_product_from_cart, name='delete_product_from_cart'),
    path('clear/', clear_cart, name='clear_cart')
]
