from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
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
            raise forms.ValidationError('Пароли не совпадают')
        if len(cd['password2']) < 8:
            raise forms.ValidationError('Пароль должен состоять минимум из 8 символов')
        return cd['password2']

    def clean_email(self):
        cd = self.cleaned_data
        email = cd['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return cd['email']


class PasswordResetFormMy(PasswordResetForm):

    def clean_email(self):
        cd = self.cleaned_data
        email = cd['email']
        if not User.objects.filter(email=email):
            raise forms.ValidationError('Пользователь с таким email не зарегестрирован')
        return cd['email']



class Set_new_password_form(SetPasswordForm):

    def clean_new_password2(self):
        cd = self.cleaned_data
        if cd['new_password1'] != cd['new_password2']:
            raise forms.ValidationError('Пароли не совпадают')
        if len(cd['new_password2']) < 8:
            raise forms.ValidationError('Пароль должен состоять минимум из 8 символов')
        return cd['new_password2']
