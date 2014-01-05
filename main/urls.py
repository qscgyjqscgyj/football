# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from main.views import MainView, SupernumeraryDetailView, RobokassaError, RobokassaSuccess, RobokassaFail, robokassa_result


urlpatterns = patterns('',
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^supernumerary/(?P<pk>\d+)$', SupernumeraryDetailView.as_view(), name='supernumerary'),
    url(r'^package/result$', robokassa_result, name='robokassa_result'),
    url(r'^package/success$', RobokassaSuccess.as_view(), name='robokassa_success'),
    url(r'^package/fail$', RobokassaFail.as_view(), name='robokassa_fail'),
)
