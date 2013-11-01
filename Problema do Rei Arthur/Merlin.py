# -*- coding: utf-8 -*-
#EP2 PALOMA E LUCAS SHEN
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
    txt = arq.readlines() #Cria uma lista pra cada linha do arquivo
    aux_d = 0
    dic = {}
    for i in txt: #Pra cada linha cria um valor no dicionario
        linha = txt[aux_d].split()
        dic[linha[0]] = linha[1:] #O dicionario recebe como chave a pessoa que possue favoritos e os valores são os favoritos
        aux_d += 1
    arq.close()
    return dic

def casamento(damasEPreferidos):
    for k in enumeracoes(damasEPreferidos.keys()):
        casado = []
        for i in k:
            j = 0
            qtdCavaleiros = len(damasEPreferidos[i])
            if qtdCavaleiros == 1: #Verifica se temos apenas um pretendente
                if damasEPreferidos[i][j] not in casado: #Caso o pretende não esteja na lista, casa ele
                    casado.append(damasEPreferidos[i][j])
                else: #Se tiver na lista quer dizer q não tem como casar, pq só tem 1 pretendente
                     return "Casamento não é possivel, "
            while j < qtdCavaleiros: #Enquanto tiver cavaleiros ele roda
                if damasEPreferidos[i][j] not in casado: #Caso o pretende não esteja na lista, casa ele e quebra o WHILE
                    casado.append(damasEPreferidos[i][j])
                    break
                j += 1
    return ("Casamento possivel, ")

#Chamadas dos metodos
dicCasamento = arquivo("C:\Users\Shen\PycharmProjects\ED\Problema do Rei Arthur\casamento.txt")
cavaleirosEPreferidos = arquivo("C:\Users\Shen\PycharmProjects\ED\Problema do Rei Arthur\cavaleiros.txt")
cavaleiros = cavaleirosEPreferidos.keys()

print(casamento(dicCasamento))

for p in permutacoes(cavaleiros):
    if p[1] in cavaleirosEPreferidos[p[0]] and p[2] in cavaleirosEPreferidos[p[1]] \
        and p[3] in cavaleirosEPreferidos[p[2]] and p[4] in cavaleirosEPreferidos[p[3]] \
        and p[5] in cavaleirosEPreferidos[p[4]] and p[6] in cavaleirosEPreferidos[p[5]] \
        and p[0] in cavaleirosEPreferidos[p[6]]:
        print("Mesa: %s" % p[0:7])
        break
    else:
        continue