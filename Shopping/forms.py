from django import forms
from django.forms import ModelForm
from Booking.models.booking import Booking
from Shopping.models.customer import Customer
from Shopping.models.profile import Profile
from django import forms
from django.contrib.auth.models import User


class updatecustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'username', 'phone', 'email', 'images', 'age', 'address']


class updateprofile(ModelForm):
    class Meta:
        model = Profile
        fields = ('address', 'age', 'images')
        lables = {
            'address': '',
            'age': '',
            'images': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'FullName'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        }
