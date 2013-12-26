# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from user_profile.models import *


class SupernumeraryChangeForm(UserChangeForm):

    class Meta:
        model = Supernumerary


class SupernumeraryAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'fio', )
    form = SupernumeraryChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('fio', 'photo', 'right', 'wrong', 'about', 'users')}),
    )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'fio', )
    form = CustomUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('fio', 'left', 'used', 'packages')}),
    )

admin.site.register(Supernumerary, SupernumeraryAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

