# -*- coding: utf-8 -*-
import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView
from game.forms import ForecastForm
from game.models import *
import datetime
from user_profile.models import CustomUser


class GameListView(ListView):
    template_name = 'games.html'
    model = Game

    def get_context_data(self, **kwargs):
        context = super(GameListView, self).get_context_data(**kwargs)
        games_list = []
        games = Game.objects.all()
        for game in games:
            eventdate = datetime.datetime(game.date.year, game.date.month, game.date.day, game.date.hour,
                                          game.date.minute)
            games_list.append(
                {
                    'title': game.__unicode__(),
                    'start': eventdate.isoformat(),
                    'url': '/game/' + str(game.pk),
                }
            )
        context['games'] = json.dumps(games_list)
        return context


class GameDetailView(DetailView):
    model = Game
    template_name = "game.html"
    context_object_name = "game"
    pk_url_kwarg = "pk"


class NewForecastView(FormView):
    template_name = 'forecast.html'
    success_url = '/forecast/new'
    form_class = ForecastForm

    def get_context_data(self, **kwargs):
        context = super(NewForecastView, self).get_context_data(**kwargs)
        user = self.request.user
        try:
            custom_user = CustomUser.objects.get(pk=user.pk).pk
        except ObjectDoesNotExist:
            custom_user = False
        if user.pk == custom_user:
            context['custom_user'] = True
        return context

    def form_valid(self, form_class):
        if self.request.method == 'POST':
            if form_class.is_valid():
                message = form_class.save()
                message.supernumerary = self.request.user.supernumerary
                message.save()
            return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self):
        kwargs = super(NewForecastView, self).get_form_kwargs()
        games = []
        all_games = Game.objects.all()
        try:
            supernumerary = self.request.user.supernumerary
            forecasts = Forecast.objects.filter(supernumerary=supernumerary)
            for game in all_games:
                for forecast in forecasts:
                    if game == forecast.game:
                        games.append(game.pk)
            self.form_class.base_fields['game'].queryset = Game.objects.exclude(id__in=games)
            return kwargs
        except ObjectDoesNotExist:
            return kwargs