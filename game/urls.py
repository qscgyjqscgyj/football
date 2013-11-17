# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from game.views import GameListView


urlpatterns = patterns('',
    url(r'^games$', GameListView.as_view(), name='game_list'),
)
