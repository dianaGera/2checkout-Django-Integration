from django import forms
from .models import Plan, Payment
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class PaymentForm(forms.Form):
    cc_number = CardNumberField(label='Card Number',)
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')



           