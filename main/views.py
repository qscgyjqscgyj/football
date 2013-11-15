# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from slider.models import Slider


class MainView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data()
        context['slides'] = Slider.objects.all()
        return context