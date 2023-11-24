from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput

from customer.models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),



        }
