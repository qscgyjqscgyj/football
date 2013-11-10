# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from news.views import NewsListView, NewView


urlpatterns = patterns('',
    url(r'^news$', NewsListView.as_view(), name='news'),
    url(r'^new/(?P<pk>\d)$', NewView.as_view(), name='new'),
)
