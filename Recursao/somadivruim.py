# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

__author__ = 'lucas.shen'
#EXERCICIO 6 LISTA RECURSÃO
def f(x, y):
    if x >= y:
        return float((x + y) / 2)
    else:
        return float(f(f(x + 2, y - 1), f(x + 1, y - 2)))


print(f(1, 10))