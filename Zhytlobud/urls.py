"""
Definition of urls for Zhytlobud
$ python manage.py makemigrations tutorial
$ python manage.py migrate tutorial

$ python manage.py inspectdb

heroku run python manage.py migrate

heroku run python manage.py createsuperuser -a zhytlobud

heroku run python manage.py makemigrations -a zhytlobud
heroku run python manage.py migrate -a zhytlobud

python manage.py dumpdata > db.json

on heroku: heroku run python manage.py loaddata db.json -a zhytlobud

DELETE ALL SUPERUSERS IF THERE IS PROBLEM!!

> python manage.py shell
$ from django.contrib.auth.models import User
$ User.objects.get(username="joebloggs", is_superuser=True).delete()

heroku ps
heroku ps:stop run.4859
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


   path("update_menu/", views.update_menu, name="update_menu"),
   path("object_menu/", views.object_menu, name="object_menu"),
   path("customer_menu/", views.customer_menu, name="customer_menu"),
   path("other_menu/", views.other_menu, name="other_menu"),
   url(r'^register/$', views.register, name='register'),

   path("customers_add/", views.customers_add, name="customers_add"),
   path("customers_edit/", views.customers_edit, name="customers_edit"),
   path("customers_edit_values/", views.customers_edit_values, name="customers_edit_values"),

   path("building_add/", views.building_add, name="building_add"),
   path("objects_edit/", views.objects_edit, name="objects_edit"),
   path("objects_review/", views.objects_review, name="objects_review"),
   path("object_edit_complex/", views.object_edit_complex, name="object_edit_complex"),

   #For Ajax. Look at script in building_add.html.
   url(r'^ajax/getStreets/$', views.getStreets, name='getStreets'),
   url(r'^ajax/getSubways/$', views.getSubways, name='getSubways'),
   url(r'^ajax/getCityAreas/$', views.getCityAreas, name='getCityAreas'),
   url(r'^ajax/getSection/$', views.getSection, name='getSection'),
]
