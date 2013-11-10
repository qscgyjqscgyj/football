# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from news.models import News


class NewsListView(ListView):
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = News.objects.all()


class NewView(DetailView):
    model = News
    template_name = "new-details.html"
    context_object_name = "new"
    pk_url_kwarg = "pk"