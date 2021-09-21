from django.contrib.auth.models import User
from django import forms
from .models import *

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={"class": 'username'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'first_name'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={"class": 'last_name'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class": 'email'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "password"}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput({"class": "password"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']