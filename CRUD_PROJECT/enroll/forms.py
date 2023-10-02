from django import forms
from .models import User


class UserContact(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'name', 'Age', 'email', 'pincode', 'Address', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50','placeholder':'Enter Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'maxlength': '50','placeholder':'Enter Your email'}),
            'Age': forms.NumberInput(attrs={'class': 'form-control',  'maxlength': '2','placeholder':'enter your age'}),
            'pincode': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '10','placeholder':'enter your pin-code'}),
            'Address': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '255','placeholder':'Enter your address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '15','placeholder':'enter Contact Number'}),
        }