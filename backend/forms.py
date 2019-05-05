from django import forms
from .models import *
class RegisterForm(forms.Form):
    payment_date = forms.DateField()
    pay_inSlip = forms.ImageField()
    user_email = forms.EmailField(max_length=254)

class DriverForm(forms.ModelForm):
        class Meta:
        model = Driver
        exclude = ['team_id', 'driver_id']