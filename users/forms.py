from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=4,
                               widget=forms.TextInput({"class":"form-control"}))

    password = forms.CharField(widget=forms.PasswordInput({"class":"form-control",
                                                           "type":"password"}))


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=4,
                               widget=forms.TextInput({"class": "form-control"}))

    first_name = forms.CharField(max_length=100, min_length=4,
                               widget=forms.TextInput({"class": "form-control"}))

    lastname = forms.CharField(max_length=100, min_length=4,
                               widget=forms.TextInput({"class": "form-control"}))

    email = forms.CharField(max_length=100, min_length=4,
                               widget=forms.TextInput({"class": "form-control",
                                                       "type": "email"}))

    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control",
                                                           "type": "password"}))

    confirm_password = forms.CharField(widget=forms.PasswordInput({"class": "form-control",
                                                           "type": "password"}))

