from django import forms
from .models import CallBooking

class CallBookingForm(forms.ModelForm):
    class Meta:
        model = CallBooking
        fields = ['name', 'phone', 'email', 'date']
        
class ChatForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label='Your Message')

class PredictionForm(forms.Form):
    bmi = forms.FloatField(label='BMI')
    blood_pressure = forms.FloatField(label='Blood Pressure')
