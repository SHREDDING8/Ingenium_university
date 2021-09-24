from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.

class Profile(View):
    def get(self,request):
        if request.user.is_authenticated:
            print(dir(request.user))
            return HttpResponse(
                """Здесь будет личный кабинет <br>
                <a href="logout/">
                        Выйти
                    </a>
                """
            )
        else:
            return HttpResponse(
                """Вы не вошли в систему <br>
                <a href="login/">
                        Войти
                    </a>
                """
            )




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
            return redirect('login')
        else:
            render_file = 'registration/register.html'
            values = {
                'user_form': user_form,
                'header': True,
            }
            errors = []
            print(dir(user_form.errors))
            try:
                passwrod2_error = dict(user_form.errors)['password2']
                errors.append(passwrod2_error[0])
            except:
                pass

            try:
                login_error = dict(user_form.errors)['username']
                errors.append(login_error[0])
            except:
                pass

            values['errors'] = errors
            return render(request, render_file, values)
