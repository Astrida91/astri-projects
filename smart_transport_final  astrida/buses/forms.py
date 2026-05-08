from django import forms
from .models import Bus,Payment

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['name', 'plate_number', 'capacity', 'driver', 'route', 'is_active']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount']  # You might want to display the amount for payment, or keep it hidden if payment amount is predefined