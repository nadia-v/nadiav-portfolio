from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(required=True)
