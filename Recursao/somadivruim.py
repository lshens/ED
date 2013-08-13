# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
__author__ = 'lucas.shen'
#EXERCICIO 6 LISTA RECURSÃO
def fr(x, y):
    #print(x, '|', y)
    if x >= y:
        return float((x + y)/2)
    else:
        return float(fr(fr(x + 2, y - 1), fr(x + 1, y - 2)))

def fb(x, y):
    #print(x, '|', y)
    if x >= y:
        return float((x + y)/2)
    else:
        return float(fb(x + 2.5, y - 2.5))

print(fr(3, 10), 'F - RUIM')
print(fb(3, 10), 'F-BOM')