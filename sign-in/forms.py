from django import forms

# https://docs.djangoproject.com/en/3.1/topics/forms/

class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
