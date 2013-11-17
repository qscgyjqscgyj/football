# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from game.models import *


class GameListView(ListView):
    template_name = 'games.html'
    model = Game

    def get_context_data(self, **kwargs):
        context = super(GameListView, self).get_context_data(**kwargs)
        games = []
        context['games'] = games
        return context



#class GameDetailView(DetailView):
#    model = Game
#    template_name = "new-details.html"
#    context_object_name = "new"
#    pk_url_kwarg = "pk"