from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'order_note']
        # widgets is the front html input appearance for example we can set the rows of the input of order_note to 3,
        # and it has nothing to do with real form, backend, or database
        widgets = {
            'address': forms.Textarea(attrs={'row': 2}),
            'order_note': forms.Textarea(attrs={'row': 2}),
        }
