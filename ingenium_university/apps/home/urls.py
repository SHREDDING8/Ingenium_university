"""ingenium_university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home.as_view(), name='home'),  # главная страница
    path("form/callback", views.CallBack.as_view(), name='callback'),

    path("about/", views.About.as_view(), name='about'),
    path("about/review", views.Review_request.as_view(), name='review'),

    path("courses/", views.Courses_view.as_view(), name='courses'),
    path("course/<int:id>", views.Course_view.as_view(), name='course_view'),

    path("webinars/", views.Webinars_View.as_view(), name='webinars'),
    path("webinar/<int:id>", views.Webinar_watch_View.as_view(), name='webinar_watch'),
    path("lk/", views.lk, name='lk'),

]
