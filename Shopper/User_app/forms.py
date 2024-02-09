from django import forms
from .models import User


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
