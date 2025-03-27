from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['email', 'text']
        widgets = {

            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Phone"}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Message"}),
        }