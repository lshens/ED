# -*- coding: utf-8 -*-
#Lucas Shen e Paloma exercicio E 5.22
from random import choice

def minimo(grafo):
    v = choice()
    mi = g[v]
    for i in grafo:
        if len(grafo[i]) < len(mi):
            mi = grafo[i]
            v = i
        if len(grafo[i]) == len(mi):
            if i < v:
                mi = grafo[i]
                v = i
    return v

def remove_all(vertice):
    for i in g:
        if vertice in g[i]:
            g[i].remove(vertice)

g = {}
g[1] = [6, 7]
g[2] = [3, 7]
g[3] = [2, 4, 6, 7]
g[4] = [3, 7]
g[5] = [7]
g[6] = [1, 3]
g[7] = [1, 2, 3, 4, 5]

x = []
#h = g
#removidos = [False,False,False,False,False,False,False]
#v_next = []

#v = minimo(g) # pega o minimo
#v_next = g.get(7)
#print(g)
#g.pop(v) #remove o vertice
#g.pop(min(v_next)) #  remove o seguinte



#print(g)
#print(v_next.pop(min(v_next)))
#print(v_next)
#print(g)
y = 0
while g != {}:
    v = minimo(g) #recebe o minimo
    e = g[v]
    x.append(v) #coloco na lista de resultado
    remove_all(v) #remove o minimo de todas as arestas
    g.pop(v) #remove o vertice do grafo
    while y != len(e):
        remove_all(e[y]) #remove o valor da aresta do grafo
        g.pop(e[y]) #remove vertice do grafo
        e.pop(y) #remove da lista de aresta
print(x)
#print(g)



