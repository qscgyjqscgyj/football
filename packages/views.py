# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from robokassa.forms import RobokassaForm
from packages.models import Package, UserPackage
from user_profile.models import Supernumerary


class PackagesListView(ListView):
    model = Package
    template_name = 'packages.html'
    context_object_name = 'packages'


def create_user_package(request, pk):
    package = Package.objects.get(pk=int(pk))
    if request.method == 'POST' and request.POST['supernumerary'] != 'none':
        supernumerary = Supernumerary.objects.get(pk=int(request.POST['supernumerary']))
        try:
            user_package = UserPackage.objects.create(user=request.user.customuser, package=package,
                                                      predictions=package.forecasts, supernumerary=supernumerary)
            return pay_with_robokassa(request, user_package.pk)
        except ObjectDoesNotExist and AttributeError:
            return HttpResponseRedirect('/')
    else:
        return render(request, 'package-detail.html', {'supernumerary_error': True, 'package': package,
                                                       'supernumeraries': Supernumerary.objects.all()})


class PackageDetailView(DetailView):
    model = Package
    template_name = 'package-detail.html'
    context_object_name = 'package'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(PackageDetailView, self).get_context_data(**kwargs)
        context['supernumeraries'] = Supernumerary.objects.all()
        return context


def pay_with_robokassa(request, order_pk):
    order = get_object_or_404(UserPackage, pk=UserPackage.objects.get(pk=order_pk).pk)
    form = RobokassaForm(initial={'OutSum': order.package.price, 'InvId': order.pk, 'Desc': 'test',
                                  'Email': order.user.email, 'MrchLogin': 'newtopbet'})
                # 'IncCurrLabel': '',
                # 'Culture': 'ru'

    return render(request, 'pay_with_robokassa.html', {'form': form})