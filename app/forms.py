"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import *


from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Логин')
    first_name = forms.CharField(label='Имя')
    email = forms.CharField(label='Электронная почта')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'autocomplete':'on'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')


