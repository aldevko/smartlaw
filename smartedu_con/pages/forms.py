from django import forms
from . models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First_name',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last_name',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Phone',
    }))
    message = forms.CharField(widget=forms.Textarea (attrs={
        'class': 'form-control',
        'placeholder': 'Your Message',
    }))

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']