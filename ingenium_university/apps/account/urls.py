from django.urls import path, include
from django.contrib.auth import views as authViews
from . import views
from .forms import PasswordResetFormMy, Set_new_password_form

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('PasswordReset/',
         authViews.PasswordResetView.as_view(form_class=PasswordResetFormMy,
                                             extra_context={'header': True}),
         name='reset'),
    path('PasswordReset/Done/',
         authViews.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html',
                                                 extra_context={'header': True}),
         name='password_reset_done'),
    path('set_new_password/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(extra_context={'header': True},
                                                                               form_class=Set_new_password_form),
         name='password_reset_confirm'),
    path('set_new_password/complete/', authViews.PasswordResetCompleteView.as_view(extra_context={'header': True}), name='password_reset_complete')
]
