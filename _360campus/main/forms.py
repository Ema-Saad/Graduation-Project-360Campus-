from django import forms
from django.contrib.auth.forms import AuthenticationForm

class StudentLoginForm(forms.Form):
    username = forms.CharField(label="Email or UNIID", max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
