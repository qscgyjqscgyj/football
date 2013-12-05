# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from user_profile.models import *


class SupernumeraryChangeForm(UserChangeForm):

    class Meta:
        model = Supernumerary


class CustomAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'fio', )
    form = SupernumeraryChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('fio', 'photo', 'right', 'wrong', 'about')}),
    )

admin.site.register(Supernumerary, CustomAdmin)
admin.site.register(CustomUser)

