# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, DetailView
from slider.models import Slider
from game.models import Game, Forecast
from user_profile.models import Supernumerary


class Foo(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name.decode('utf-8')

    def __repr__(self):
        return '%s' % self.name


class MainView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data()
        context['slides'] = Slider.objects.all()
        context['games'] = Game.objects.all()
        supernumeraries = []
        for supernumerary in Supernumerary.objects.all().order_by('-right'):
            supernumerary.right_forecasts = len(Forecast.objects.filter(supernumerary=supernumerary, right=True))
            supernumerary.wrong_forecasts = len(Forecast.objects.filter(supernumerary=supernumerary, wrong=True))
            supernumeraries.append(supernumerary)
        context['supernumeraries'] = [supernumeraries[0], supernumeraries[1]]
        return context


class SupernumeraryDetailView(DetailView):
    model = Supernumerary
    template_name = 'supernumerary.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'supernumerary'

    def get_context_data(self, **kwargs):
        context = super(SupernumeraryDetailView, self).get_context_data(**kwargs)
        context['graph'] = []
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
        self.object.right_forecasts = len(Forecast.objects.filter(supernumerary=self.object, right=True))
        self.object.wrong_forecasts = len(Forecast.objects.filter(supernumerary=self.object, wrong=True))
        return context