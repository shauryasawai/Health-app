from django import forms
from .models import CallBooking

class CallBookingForm(forms.ModelForm):
    class Meta:
        model = CallBooking
        fields = ['name', 'phone', 'email', 'date']
