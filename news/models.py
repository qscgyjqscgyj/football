# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class News(models.Model):
    name = models.CharField(verbose_name=_(u'Название новости'), max_length=100)
    date = models.DateTimeField(verbose_name=_(u'Дата новости'), auto_now_add=True, null=True)
    text = models.TextField(verbose_name=_(u'Текст новости'))
    subtext = models.CharField(verbose_name=_(u'Подтекст новости'), max_length=100)
    image = models.ImageField(verbose_name=_(u'Изображение новости'), upload_to="news")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Новость')
        verbose_name_plural = _(u'Новости')
