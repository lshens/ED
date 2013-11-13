# -*- coding: utf-8 -*-

def geraMatriz(tupla):
    lista = tupla.split()
    #Variaveis auxiliares
    linhaMatriz = []
    matriz = []
    for linha in range(len(lista)): #percorre pelo numero de linhas
        for coluna in range(len(lista[0])): #percorre pelo numero de colunas
            linhaMatriz.append(lista[linha][coluna]) #adiciona na lista
        matriz.append(linhaMatriz)
        linhaMatriz = [] #zera a lista para uma nova linha
    return matriz

def imprimiMatriz(matriz):
    for i in range(len(matriz)):
        aux = ''
        for j in range(len(matriz[i])):
            aux = aux + str(matriz[i][j])
        print(aux)

def percorre(matriz):
    #A matriz é varrida de cima(linha[0]) para baixo(linha[n]) e
    #da esquerda(coluna[0] para a direita[n]
    aux = []
    cont = 1
    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            #Se um "pixel" tem valor 1, verificamos seu vizinho de cima e da esquerda
            if matriz[linha][coluna] == 1:
                #Se ambos são ZERO, um novo objeto começa neste pixel
                if matriz[linha -1][coluna] and matriz[linha][coluna - 1] == 0:
                    aux.append(matriz[linha][coluna])
                #Se um deles é 1, este pixel pertence ao objeto anterior
                if matriz[linha -1][coluna] or matriz[linha][coluna - 1] == 1:
                    aux.append(matriz[linha][coluna])

t = '''101
       111
       000
       101'''

print("Entrada:")
imprimiMatriz(geraMatriz(t))


