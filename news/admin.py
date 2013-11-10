# -*- coding: utf-8 -*-
from django.contrib import admin
from news.forms import NewsForm
from news.models import *


class NewsAdmin(admin.ModelAdmin):
    form = NewsForm


admin.site.register(News, NewsAdmin)
