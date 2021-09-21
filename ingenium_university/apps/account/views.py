from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.contrib.auth.models import User


# Create your views here.

class Registration(View):
    def get(self, request):
        user_form = UserRegistrationForm()
        render_file = 'registration/register.html'
        values = {
            'user_form': user_form,
            'header': True,
        }
        return render(request, render_file, values)

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
        else:
            render_file = 'registration/register.html'
            values = {
                'user_form': user_form,
                'header': True,
            }
            errors = []
            print(dict(user_form.errors))
            try:
                passwrod2_error = dict(user_form.errors)['password2']
                errors.append('Пароли не совпадают')
            except:
                pass

            try:
                login_error = dict(user_form.errors)['username']
                errors.append(login_error[0])
            except:
                pass

            values['errors'] = errors

            print(errors)
            return render(request, render_file, values)

