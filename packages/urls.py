# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from packages.views import PackagesListView, PackageDetailView, create_user_package, pay_with_robokassa
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^packages$', PackagesListView.as_view(), name='packages_list'),
    url(r'^package/create/(?P<pk>\d+)$', login_required(create_user_package), name='create_user_package'),
    url(r'^package/pre-create/(?P<pk>\d+)$', PackageDetailView.as_view(), name='pre_crete_user_package_detail'),
    url(r'^package/pay/$', pay_with_robokassa, name='robokassa'),
)
