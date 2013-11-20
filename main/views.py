# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from slider.models import Slider
from user_profile.models import Supernumerary


class MainView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data()
        context['slides'] = Slider.objects.all()
        context['supernumeraries'] = Supernumerary.objects.all()
        return context