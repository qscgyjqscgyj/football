# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user_profile.models import *


class CustomAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'fio', 'photo',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', )

admin.site.register(Supernumerary, UserAdmin)
admin.site.register(CustomUser)

