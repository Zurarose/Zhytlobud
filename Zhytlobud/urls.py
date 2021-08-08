"""
Definition of urls for Zhytlobud
$ python manage.py makemigrations tutorial
$ python manage.py migrate tutorial

$ python manage.py inspectdb

heroku run python manage.py migrate

heroku run python manage.py createsuperuser -a zhytlobud
heroku run python manage.py migrate -a zhytlobud
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls import url

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.login, name='login'),
   path('menu/', views.menu, name='menu'),
   path("logout/", LogoutView.as_view(), name="logout"),

   path("subtabs/building_add/", views.building_add, name="building_add"),
   path("/update_menu/", views.update_menu, name="update_menu"),
   #For Ajax. Look at script in building_add.html.
   url(r'^ajax/getStreets/$', views.getStreets, name='getStreets'),
   url(r'^ajax/getSubways/$', views.getSubways, name='getSubways'),
    url(r'^ajax/getCityAreas/$', views.getCityAreas, name='getCityAreas'),
]
