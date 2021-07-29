"""
Definition of urls for Zhytlobud
$ python manage.py makemigrations tutorial
$ python manage.py migrate tutorial
$ python manage.py inspectdb
heroku run python manage.py migrate
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
   path('', views.login, name='login'),
   path('menu/', views.menu, name='menu'),
   path("logout/", LogoutView.as_view(), name="logout"),

   path("tabs/building_add/", views.building_add, name="building_add"),
]
