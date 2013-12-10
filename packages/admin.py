# -*- coding: utf-8 -*-
from django.contrib import admin
from packages.models import Package, UserPackage


admin.site.register(Package)
admin.site.register(UserPackage)
