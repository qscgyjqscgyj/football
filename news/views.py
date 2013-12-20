# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, DetailView
from news.models import News


class NewsListView(ListView):
    template_name = 'news.html'
    queryset = News.objects.all()

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        news_list = News.objects.all()
        show = 5
        news_paginator = Paginator(news_list, show)
        page = self.request.GET.get('page')
        try:
            news = news_paginator.page(page)
        except PageNotAnInteger:
            news = news_paginator.page(1)
        except EmptyPage:
            news = news_paginator.page(news_paginator.num_pages)
        context['news'] = news
        context['news_len'] = len(News.objects.all())
        context['news_all_pages'] = news_paginator.count
        context['show'] = show
        return context


class NewView(DetailView):
    model = News
    template_name = "new-details.html"
    context_object_name = "new"
    pk_url_kwarg = "pk"