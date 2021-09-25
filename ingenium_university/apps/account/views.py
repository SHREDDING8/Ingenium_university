from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.http import HttpResponse


# Create your views here.

class Profile(View):
    def get(self, request):
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
            print(new_user
                  )
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
            try:
                email_error = dict(user_form.errors)['email']
                errors.append(email_error[0])
            except:
                pass
            values['errors'] = errors
            return render(request, render_file, values)


class Reset_password(PasswordResetView):
    render_file = 'registration/password_reset_form.html'

    def get(self, request):
        form_reset = PasswordResetFormMy()

        values = {
            'form_reset': form_reset,
            "reset_email": True,
            'header': True,
        }

        return render(request, self.render_file, values)

    def post(self, request):
        form_reset = PasswordResetFormMy(request.POST)
        print(123123)
        if form_reset.is_valid():
            values = {
                'form_reset': form_reset,
                "reset_done": True,
                "reset_email": False,
                'header': True,
            }
            return render(request, self.render_file, values)
        else:
            print(1234567890)


class Reset_Password_Done(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'
