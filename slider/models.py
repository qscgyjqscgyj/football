# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Slider(models.Model):
    img = models.ImageField(upload_to='slider_img')
    title = models.CharField(verbose_name=_(u'Заголовок слайда'), max_length=100)
    text = models.TextField(verbose_name=_(u'Содержание слайда'), blank=True, null=True)
    url = models.CharField(verbose_name=_(u'Ссылка'), max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u'Слайд')
        verbose_name_plural = _(u'Слайды')
