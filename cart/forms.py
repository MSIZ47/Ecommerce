from django import forms


class AddProductToCartForm(forms.Form):
    QUANTITY = [(i,  str(i)) for i in range(1, 31)]
    quantity = forms.TypedChoiceField(choices=QUANTITY, coerce=int)
    replace_quantity = forms.BooleanField(required=False, widget=forms.HiddenInput)

