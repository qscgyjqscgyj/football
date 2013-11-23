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

    def __unicode__(self):
        return self.game.__unicode__()

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

    def save(self, *args, **kwargs):
        if self.score or self.draw or self.win_team:
            forecasts = Forecast.objects.filter(game=self)
            for forecast in forecasts:
                if forecast.score and forecast.draw and forecast.win_team:
                    supernumerary = Supernumerary.objects.get(id=forecast.supernumerary.pk)
                    supernumerary.wrong = F('wrong') + 1
                    supernumerary.save()
                elif forecast.score and forecast.draw:
                    supernumerary = Supernumerary.objects.get(id=forecast.supernumerary.pk)
                    supernumerary.wrong = F('wrong') + 1
                    supernumerary.save()
                elif forecast.draw and forecast.win_team:
                    supernumerary = Supernumerary.objects.get(id=forecast.supernumerary.pk)
                    supernumerary.wrong = F('wrong') + 1
                    supernumerary.save()
                elif forecast.score and forecast.win_team:
                    supernumerary = Supernumerary.objects.get(id=forecast.supernumerary.pk)
                    supernumerary.wrong = F('wrong') + 1
                    supernumerary.save()
                elif (forecast.score == self.score and forecast.score) or (forecast.draw == self.draw and forecast.draw) or (forecast.win_team == self.win_team and forecast.win_team):
                    supernumerary = Supernumerary.objects.get(id=forecast.supernumerary.pk)
                    supernumerary.right = F('right') + 1
                    supernumerary.save()
                else:
                    supernumerary = Supernumerary.objects.get(id=forecast.supernumerary.pk)
                    supernumerary.wrong = F('wrong') + 1
                    supernumerary.save()
        super(Game, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _(u'Игра')
        verbose_name_plural = _(u'Игры')