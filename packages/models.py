# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Package(models.Model):
    name = models.CharField(verbose_name=_(u'Название'), max_length=100)
    price = models.IntegerField(verbose_name=_(u'Стоимость'))
    forecasts = models.IntegerField(verbose_name=_(u'Количество прогнозов'))
    image = models.ImageField(verbose_name=_(u'Изображение'), upload_to='packages_images')
    about = models.TextField(verbose_name=_(u'Описание'))

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Пакет')
        verbose_name_plural = _(u'Пакеты')


class UserPackage(models.Model):
    user = models.ForeignKey('user_profile.CustomUser', verbose_name=_(u'Пользователь'),
                             related_name='user_package_custom_user')
    package = models.ForeignKey(Package, verbose_name=_(u'Пакет'), related_name='user_package_package')
    predictions = models.IntegerField(verbose_name=_(u'Оставшиеся прогнозы'))
    supernumerary = models.ForeignKey('user_profile.Supernumerary', verbose_name=_(u'Статист'),
                                      related_name='user_package_supernumerary', blank=True, null=True)
    active = models.BooleanField(verbose_name=_(u'Активен после оплаты'), default=False)

    def __unicode__(self):
        return unicode(self.user)

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Пользовательский пакет')
        verbose_name_plural = _(u'Пользовательские пакеты')
