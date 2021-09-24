from django.urls import path,include
from django.contrib.auth import views as authViews
from . import views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('profile', views.Profile.as_view(), name='profile')
]