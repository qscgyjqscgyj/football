# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, DetailView
from slider.models import Slider
from game.models import Game, Forecast
from user_profile.models import Supernumerary


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

    def get_context_data(self, **kwargs):
        context = super(SupernumeraryDetailView, self).get_context_data(**kwargs)
        context['graph'] = [['Дата', 'right', 'wrong']]
        forecasts = Forecast.objects.filter(supernumerary=self.object).order_by('game')
        right = 0
        wrong = 0
        for forecast in forecasts:
            if forecast.right:
                context['graph'].append([str(forecast.game.date.day) + '.' + str(forecast.game.date.month), right + 1, wrong])
                right += 1
            elif forecast.wrong:
                context['graph'].append([str(forecast.game.date.day) + '.' + str(forecast.game.date.month), right, wrong + 1])
                wrong += 1
        return context