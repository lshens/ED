# -*- coding: utf-8 -*-
def enumeracoes(items):
    n = len(items)
    s = [0]*(n+1)
    k = 0
    while True:
        if s[k] < n:
            s[k+1] = s[k] + 1
            k += 1
        else:
            s[k-1] += 1
            k -= 1
        if k == 0:
            break
        else:
            lista = []
            for j in range(1, k+1):
                lista.append(items[s[j]-1])
            yield lista

def combinacoes(items, n):
    if n == 0: yield []
    else:
        for i in range(len(items)):
            for cc in combinacoes(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def permutacoes(items):
    return combinacoes(items, len(items))

def arquivo(url):
    arq = open(url)
    txt = arq.readlines()
    x = 0
    f = []
    for i in txt:
        f.append(txt[x].split())
        x += 1
    return f

#print ('Permutações')
#for p in permutacoes(['Adriano','Bruno', 'Diogo', 'Eclis', 'Gabriel', 'Leandro', 'Walber']):
#    print (p)

print ('Enumerações')
for p in enumeracoes(arquivo("C:\Users\Shen\PycharmProjects\ED\Problema do Rei Arthur\casamento.txt")):
    print (p)
