from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=False, widget=forms.EmailInput)
    phone = forms.CharField(max_length=10, required=True)
    name = forms.CharField(max_length=25, required=True)


    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2', 'phone')