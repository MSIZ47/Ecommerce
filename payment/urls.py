from django.urls import path, include
from .views import payment_process, payment_callback


app_name = 'payment'
urlpatterns = [
    path('process/', payment_process, name='process'),
    path('callback/', payment_callback, name='callback'),
]
