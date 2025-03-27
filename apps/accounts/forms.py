from django import forms


from .models import *
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(

        attrs={
            'class':'from-control',
            'placeholder':'Create Password'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(

        attrs={
            'class': 'from-control',
            'placeholder': 'Repeat Password'
        }
    ))

    email = forms.CharField(widget=forms.EmailInput(

        attrs={

            'placeholder': 'Enter Email'
        }
    ))

    class Meta:
        model = User
        fields = ['email','password1','password2']


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(

        attrs={

            'placeholder': 'Enter Email'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(

        attrs={
            'class': 'from-control',
            'placeholder': 'Create Password'
        }
    ))




















