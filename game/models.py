# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from user_profile.models import Supernumerary
from django.db.models import F


class Team(models.Model):
    name = models.CharField(verbose_name=_(u'Команда'), max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Команда')
        verbose_name_plural = _(u'Команды')


class SportType(models.Model):
    name = models.CharField(verbose_name=_(u'Вид спорта'), max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Вид спорта')
        verbose_name_plural = _(u'Виды спорта')


class Forecast(models.Model):
    supernumerary = models.ForeignKey(Supernumerary, verbose_name=_(u'Статист'),
                                      related_name='forecast_supernumerary', blank=True, null=True)
    game = models.ForeignKey('Game', verbose_name=_(u'Игра'), related_name='forecast_game')
    score = models.CharField(verbose_name=_(u'Счет'), max_length=100, blank=True, null=True)
    draw = models.BooleanField(verbose_name=_(u'Ничья'))
    win_team = models.ForeignKey(Team, verbose_name=_(u'Победившая команда'), related_name='forecast_team',
                                 blank=True, null=True)
    detailed = models.CharField(verbose_name=_(u'Подробный прогноз'), max_length=100, blank=True, null=True)
    right = models.BooleanField(verbose_name=_(u'Верный прогноз'))
    wrong = models.BooleanField(verbose_name=_(u'Не верный прогноз'))

    def __unicode__(self):
        return self.game.__unicode__()

    def save(self, *args, **kwargs):
        if self.right:
            supernumerary = Supernumerary.objects.get(id=self.supernumerary.pk)
            supernumerary.right = F('right') + 1
            supernumerary.save()
        elif self.wrong:
            supernumerary = Supernumerary.objects.get(id=self.supernumerary.pk)
            supernumerary.wrong = F('wrong') + 1
            supernumerary.save()
        else:
            return super(Forecast, self).save(*args, **kwargs)
        return super(Forecast, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _(u'Прогноз')
        verbose_name_plural = _(u'Прогнозы')


class Game(models.Model):
    sport = models.ForeignKey(SportType, verbose_name=_(u'Вид спорта'), related_name='game_sport_type',
                              blank=True, null=True)
    team1 = models.CharField(verbose_name=_(u'Название первой команды'), max_length=100)
    team2 = models.CharField(verbose_name=_(u'Название второй команды'), max_length=100)
    date = models.DateTimeField(verbose_name=_(u'Начало игры'))
    win_team = models.ForeignKey(Team, verbose_name=_(u'Победившая команда'), related_name='game_team',
                                 blank=True, null=True)
    score = models.CharField(verbose_name=_(u'Счет игры'), max_length=100, blank=True, null=True)
    draw = models.BooleanField(verbose_name=_(u'Ничья'))

    def __unicode__(self):
        return (unicode(self.sport) + " " + self.team1 +
                " vs " + self.team2 + " " + str(self.date))

    class Meta:
        verbose_name = _(u'Игра')
        verbose_name_plural = _(u'Игры')
        ordering = ('date',)


class UserForecast(models.Model):
    user = models.ForeignKey('user_profile.CustomUser', verbose_name=_(u'Пользователь'),
                             related_name='user_forecast_user')
    supernumerary = models.ForeignKey('user_profile.Supernumerary', verbose_name=_(u'Статист'),
                                      related_name='user_forecast_supernumerary')
    date = models.DateTimeField(verbose_name=_(u'Дата прогноза'), auto_now_add=True)
    forecast = models.ForeignKey('Forecast', verbose_name=_(u'Прогноз специалиста'),
                                 related_name='user_forecast_forecast')
    one = models.BooleanField(verbose_name=_(u'Единичный прогноз'), default=False)
    one_package = models.ForeignKey('packages.UserPackage', verbose_name=_(u'Единичный пакет'), blank=True, null=True)

    def __unicode__(self):
        return self.forecast.__unicode__()

    class Meta:
        verbose_name = _(u'Пользовательский прогноз')
        verbose_name_plural = _(u'Пользовательские прогнозы')
        ordering = ('date',)
