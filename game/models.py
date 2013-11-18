# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from user_profile.models import Supernumerary


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


class Forecast(models.Model):
    supernumerary = models.ForeignKey(Supernumerary, verbose_name=_(u'Статист'),
                                      related_name='forecast_supernumerary')
    game = models.ForeignKey(Game, verbose_name=_(u'Игра'), related_name='forecast_game')
    score = models.CharField(verbose_name=_(u'Счет'), max_length=100, blank=True, null=True)
    draw = models.BooleanField(verbose_name=_(u'Ничья'))
    win_team = models.ForeignKey(Team, verbose_name=_(u'Победившая команда'), related_name='forecast_team',
                                 blank=True, null=True)

    def __unicode__(self):
        return self.game.__unicode__()

    class Meta:
        verbose_name = _(u'Прогноз')
        verbose_name_plural = _(u'Прогнозы')
