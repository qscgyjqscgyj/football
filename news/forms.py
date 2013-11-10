# -*- coding: utf-8 -*-
from django import forms
from redactor.widgets import RedactorEditor
from news.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        widgets = {
            'text': RedactorEditor(),
            }