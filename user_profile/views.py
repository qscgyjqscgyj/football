# -*- coding: utf-8 -*-
import hashlib
import random
from django.utils import timezone
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.views import password_change
from django.contrib.sites.models import Site, RequestSite
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import UpdateView
from registration import signals
from registration.models import RegistrationProfile
from user_profile.forms import *
from user_profile.models import *
from registration.backends.default.views import RegistrationView
from django.contrib.auth import authenticate, login


class CustomRegistrationView(RegistrationView):
    form_class = CustomRegistrationForm

    def register(self, request, **cleaned_data):
        username = cleaned_data['username']
        email = cleaned_data['email']
        password = cleaned_data['password1']
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        new_user = self.create_inactive_user(username, email, password, site)

        user_log = authenticate(username=username, password=password)
        login(request, user_log)

        signals.user_registered.send(sender=self.__class__, user=new_user, request=request)

        return new_user

    @classmethod
    def create_user(cls, username, email, password=None, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = UserManager.normalize_email(email)
        user = User(username=username, email=email, is_staff=False, is_active=True, is_superuser=False,
                    last_login=now, date_joined=now, **extra_fields)

        user.set_password(password)
        user.save()
        return user

    def create_inactive_user(self, username, email, password, site, send_email=True):
        new_user = self.create_user(username, email, password)
        new_user.is_active = False
        new_user.save()

        registration_profile = self.create_profile(new_user)

        if send_email:
            registration_profile.send_activation_email(site)

        return new_user

    @classmethod
    def create_profile(cls, new_user):
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        username = new_user.username
        if isinstance(username, unicode):
            username = username.encode('utf-8')
        activation_key = hashlib.sha1(salt+username).hexdigest()
        return RegistrationProfile.objects.create(user=new_user, activation_key=activation_key)


class CustomUserRegistrationView(CustomRegistrationView):

    @classmethod
    def create_user(cls, username, email, password=None, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = UserManager.normalize_email(email)
        user = CustomUser(username=username, email=email, is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)

        user.set_password(password)
        user.save()
        return user


class CustomProfileView(UpdateView):
    model = User
    context_object_name = 'profile'
    success_url = '/accounts/profile/'

    def get_object(self, queryset=None):
        try:
            obj = self.request.user.supernumerary
            self.form_class = SupernumeraryProfileForm
            return obj
        except ObjectDoesNotExist:
            obj = self.request.user.customuser
            self.form_class = CustomUserProfileForm
            return obj


def my_change_password(request):
    return password_change(request, post_change_redirect='/accounts/password_change_done/')
