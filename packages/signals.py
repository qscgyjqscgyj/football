# -*- coding: utf-8 -*-
from robokassa.signals import result_received, fail_page_visited
from packages.models import UserPackage


def payment_received(sender, **kwargs):
    user_package = UserPackage.objects.get(id=kwargs['InvId'])
    user_package.active = True
    user_package.save()


def payment_fail(sender, **kwargs):
    user_package = UserPackage.objects.get(id=kwargs['InvId'])
    user_package.delete()

result_received.connect(payment_received)