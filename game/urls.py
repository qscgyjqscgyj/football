# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from game.views import GameListView, GameDetailView


urlpatterns = patterns('',
    url(r'^games$', GameListView.as_view(), name='game_list'),
    url(r'^game/(?P<pk>\d+)$', GameDetailView.as_view(), name='game_detail'),
)
