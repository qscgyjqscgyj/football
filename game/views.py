# -*- coding: utf-8 -*-
import json
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mass_mail, send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from robokassa.forms import RobokassaForm
from football.local import EMAIL_HOST_USER
from game.forms import ForecastForm
from game.models import *
import datetime
from packages.models import UserPackage, Package
from user_profile.models import CustomUser
from django.template import Context
from django.db.models import F


class GameListView(ListView):
    template_name = 'games.html'
    model = Game

    def get_context_data(self, **kwargs):
        context = super(GameListView, self).get_context_data(**kwargs)
        games_list = []
        games = Game.objects.all()
        for game in games:
            eventdate = datetime.datetime(game.date.year, game.date.month, game.date.day, game.date.hour,
                                          game.date.minute)
            games_list.append(
                {
                    'title': game.__unicode__(),
                    'start': eventdate.isoformat(),
                    'url': '/game/' + str(game.pk),
                }
            )
        context['games'] = json.dumps(games_list)
        return context


class GameDetailView(DetailView):
    model = Game
    template_name = "game.html"
    context_object_name = "game"
    pk_url_kwarg = "pk"


class NewForecastView(FormView):
    template_name = 'forecast.html'
    success_url = '/accounts/profile'
    form_class = ForecastForm

    def get_context_data(self, **kwargs):
        context = super(NewForecastView, self).get_context_data(**kwargs)
        user = self.request.user
        try:
            custom_user = CustomUser.objects.get(pk=user.pk).pk
        except ObjectDoesNotExist:
            custom_user = False
        if user.pk == custom_user:
            context['custom_user'] = True
        return context

    def form_valid(self, form_class):
        if self.request.method == 'POST':
            if form_class.is_valid():
                message = form_class.save()
                message.supernumerary = self.request.user.supernumerary
                message.save()
                users = self.request.user.supernumerary.users.all()
                for user in users:
                    try:
                        user_package = UserPackage.objects.get(user=user, supernumerary=message.supernumerary,
                                                               active=True)
                        if user_package:
                            if user_package.predictions > 0:
                                send_mail('Hi ' + user.username, "I'm The Dude! So that's what you call me.",
                                          EMAIL_HOST_USER, [user.email], fail_silently=False)
                                user_package.predictions = F('predictions') - 1
                                user_package.save()
                                forecast = Forecast.objects.get(supernumerary=message.supernumerary,
                                                                game=Game.objects.get(pk=int(self.request.POST['game']))
                                                                )
                                UserForecast.objects.create(user=user, supernumerary=message.supernumerary,
                                                            forecast=forecast)
                                # context = Context({
                                #     'name': user.username,
                                #     'user_forecast': user_forecast,
                                # })
                            else:
                                user_package.delete()
                                continue
                    except ObjectDoesNotExist:
                        continue
                return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self):
        kwargs = super(NewForecastView, self).get_form_kwargs()
        games = []
        all_games = Game.objects.all()
        try:
            supernumerary = self.request.user.supernumerary
            forecasts = Forecast.objects.filter(supernumerary=supernumerary)
            for game in all_games:
                for forecast in forecasts:
                    if game == forecast.game and game.date < datetime.datetime.now():
                        games.append(game.pk)
            self.form_class.base_fields['game'].queryset = Game.objects.exclude(id__in=games)
            return kwargs
        except ObjectDoesNotExist:
            return kwargs


def pay_for_one_forecast(request, order_pk):
    order = get_object_or_404(UserPackage, pk=UserPackage.objects.get(pk=order_pk).pk)
    form = RobokassaForm(initial={'OutSum': order.package.price, 'InvId': order.pk, 'Desc': 'test',
                                  'Email': order.user.email, 'MrchLogin': 'newtopbet'})
                # 'IncCurrLabel': '',
                # 'Culture': 'ru'

    return render(request, 'pay_with_robokassa.html', {'form': form})


def buy_forecast(request, pk):
    game = Game.objects.get(pk=int(pk))
    supernumeraries = []
    for forecast in Forecast.objects.all():
        if forecast.game == game:
            supernumeraries.append(forecast.supernumerary)
    if request.method == 'POST' and request.POST['supernumerary'] != 'none':
        supernumerary = Supernumerary.objects.get(pk=int(request.POST['supernumerary']))
        try:
            user_forecast = UserForecast.objects.create(user=request.user.customuser, supernumerary=supernumerary,
                                                        forecast=Forecast.objects.get(supernumerary=supernumerary, game=game))
            user_forecast.save()
            user_package = UserPackage.objects.create(user=request.user.customuser,
                                                      package=Package.objects.get(one=True),
                                                      predictions=1, supernumerary=supernumerary)
            return pay_for_one_forecast(request, user_package.pk)
        except ObjectDoesNotExist and AttributeError:
            return HttpResponseRedirect('/')
    else:
        return render(request, 'buy-forecast.html', {'supernumerary_error': True, 'game': game,
                                                     'package': Package.objects.get(one=True),
                                                     'supernumeraries': supernumeraries})
