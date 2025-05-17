from django import forms
from django.forms import ModelForm
from Booking.models.booking import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ('fullname', 'phone', 'address', 'time', 'date', 'playing_hours')
        labels = {
            'fullname': '',
            'phone': '',
            'address': '',
            'time': '',
            'date': '',
            'playing_hours': '',
        }
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Time'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'playing_hours': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Playing Hours'}),
        }


class AddBooking(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['fullname', 'phone', 'address', 'time', 'date', 'playing_hours']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your Full Name'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Enter your Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your Address'}),
            'time': forms.TimeInput(attrs={'class': 'form-control','placeholder':'Use HH:MM:SS format (02:02:02)'}),
            'date': forms.DateInput(attrs={'class': 'form-control','placeholder':'Use YYYY-MM-DD format (2022-03-01)'}),
            'playing_hours': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Enter your Playing Hours'}),
        }
