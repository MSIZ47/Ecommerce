from django.urls import path, include
from .views import order_view


app_name = 'order'
urlpatterns = [
    path('create/', order_view, name='order_view'),
]
