# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from registration.forms import RegistrationForm
from django import forms
from user_profile.models import *


class CustomRegistrationForm(RegistrationForm):
    captcha = CaptchaField()


class SupernumeraryProfileForm(forms.ModelForm):

    class Meta:

        def __init__(self):
            pass

        model = Supernumerary
        exclude = ('password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'first_name', 'last_name',
                   'is_staff', 'is_active', 'date_joined', 'right', 'wrong', 'users')


class CustomUserProfileForm(forms.ModelForm):

    class Meta:

        def __init__(self):
            pass

        model = CustomUser
        exclude = ('password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'first_name', 'last_name',
                   'is_staff', 'is_active', 'date_joined', 'left', 'used', 'packages', )