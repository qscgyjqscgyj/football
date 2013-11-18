# -*- coding: utf-8 -*-
import json
from django.views.generic import ListView, DetailView
from game.models import *
import datetime


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