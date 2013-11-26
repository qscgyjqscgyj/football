# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, DetailView
from slider.models import Slider
from user_profile.models import Supernumerary
from game.models import Game

class MainView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data()
        context['slides'] = Slider.objects.all()
        context['games'] = Game.objects.all()
        context['supernumeraries'] = Supernumerary.objects.all()
        return context


class SupernumeraryDetailView(DetailView):
    model = Supernumerary
    template_name = 'supernumerary.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'supernumerary'