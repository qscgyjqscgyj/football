# -*- coding: utf-8 -*-
import random


def random_digit_challenge():
    ret = u''
    for i in range(4):
        ret += str(random.randint(0, 9))
    return ret, ret