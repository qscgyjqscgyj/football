# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


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
    team1 = models.CharField(verbose_name=_(u'Название первой команды'), max_length=100)
    team2 = models.CharField(verbose_name=_(u'Название второй команды'), max_length=100)
    score = models.CharField(verbose_name=_(u'Счет игры'), max_length=100, blank=True, null=True)
    draw = models.BooleanField(verbose_name=_(u'Ничья'))
    win_team = models.ForeignKey(Team, verbose_name=_(u'Победившая команда'), related_name='game_team')
    sport = models.ForeignKey(SportType, verbose_name=_(u'Вид спорта'), related_name='game_sport_type')
    date = models.DateTimeField(verbose_name=_(u'Начало игры'))

    def __unicode__(self):
        return (str(self.sport) + str(self.team1) +
                u" - " + str(self.team2) + str(self.date))

    class Meta:
        verbose_name = _(u'Игра')
        verbose_name_plural = _(u'Игры')