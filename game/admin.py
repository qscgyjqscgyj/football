# -*- coding: utf-8 -*-
from django.contrib import admin
from game.models import *


class ForecastAdmin(admin.ModelAdmin):
    ordering = ['supernumerary']
    list_display = (Forecast.__unicode__, 'right', 'supernumerary', )


admin.site.register(Game)
admin.site.register(Team)
admin.site.register(SportType)
admin.site.register(Forecast, ForecastAdmin)
