# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from game.views import GameListView, GameDetailView, NewForecastView
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^games$', GameListView.as_view(), name='game_list'),
    url(r'^game/(?P<pk>\d+)$', GameDetailView.as_view(), name='game_detail'),
    url(r'^forecast/new$', login_required(NewForecastView.as_view(), login_url='/accounts/login/')),
)
