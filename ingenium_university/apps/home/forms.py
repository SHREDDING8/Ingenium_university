from django import forms
from django.core.exceptions import ValidationError

from .models import *


class LendingHomeForm(forms.Form):
    attrs_name = {
        'class': 'input__name',
        'placeholder': " ",
        'type': 'text'
    }
    attrs_phone = {
        'class': 'input__tel',
        'placeholder': " ",
        'type': 'tel'
    }
    attrs_email = {
        'class': 'input__email',
        'placeholder': " ",
        'type': 'email'
    }
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs=attrs_name))
    phone = forms.CharField(max_length=12, widget=forms.TextInput(attrs=attrs_phone))
    email = forms.EmailField(widget=forms.EmailInput(attrs=attrs_email))

    def clean_phone(self):
        new_phone = self.cleaned_data['phone']
        for i in new_phone:
            if i not in '1234567890+':
                raise ValidationError('неверный телефон')
        return new_phone

    def save(self):
        new_lending = LendingHome.objects.create(
            name=self.cleaned_data['name'],
            phone=self.cleaned_data['phone'],
            email=self.cleaned_data['email']
        )
        return new_lending


class ReviewFrom(forms.Form):
    review_widget = {
        'placeholder': " ",
        'rows': '1',
        'class': "review__text_input"
    }
    review = forms.CharField(widget=forms.Textarea(attrs=review_widget))

    def clean_review(self):
        review = self.cleaned_data['review']
        return review

    def save(self, first_name='Гость', second_name=''):
        new_review = Review.objects.create(
            first_name=first_name,
            second_name=second_name,
            review=self.cleaned_data['review']
        )
        return new_review
