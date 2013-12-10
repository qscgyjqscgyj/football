# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from registration.models import RegistrationManager


#статист
class Supernumerary(User):
    fio = models.CharField(verbose_name=_(u'Ф.И.О.'), max_length=100)
    photo = models.ImageField(verbose_name=_(u'Фото'), upload_to='supernumerary_photo')
    right = models.IntegerField(verbose_name=_(u'Количество верных прогнозов'), default=0)
    wrong = models.IntegerField(verbose_name=_(u'Количество неверных прогнозов'), default=0)
    about = models.TextField(verbose_name=_(u'О статисте'))
    users = models.ManyToManyField('CustomUser', verbose_name=_(u'Пользователи'), blank=True, null=True)

    objects = RegistrationManager()

    def __unicode__(self):
        return unicode(self.username)

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Статист')
        verbose_name_plural = _(u'Статисты')


#пользователь
class CustomUser(User):
    fio = models.CharField(verbose_name=_(u'Ф.И.О.'), max_length=100)
    left = models.IntegerField(verbose_name=_(u'Количество доступных прогнозов'), default=0)
    used = models.IntegerField(verbose_name=_(u'Количество использованных прогнозов'), default=0)

    objects = RegistrationManager()

    def __unicode__(self):
        return unicode(self.username)

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Пользователь')
        verbose_name_plural = _(u'Пользователи')