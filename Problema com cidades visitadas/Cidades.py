# -*- coding: utf-8 -*-
#EP3 Lucas Shen e Paloma Ribeiro
def geraMatriz(tupla):
    lista = tupla.split()
    #Variaveis auxiliares
    linhaMatriz = []
    matriz = []
    for linha in range(len(lista)): #percorre pelo numero de linhas
        for coluna in range(len(lista[0])): #percorre pelo numero de colunas
            linhaMatriz.append(int(lista[linha][coluna])) #adiciona na lista
        matriz.append(linhaMatriz)
        linhaMatriz = [] #zera a lista para uma nova linha
    print(matriz)
    return matriz

def imprimiMatriz(matriz):
    for i in range(len(matriz)):
        saida = ''
        for j in range(len(matriz[i])):
            saida = saida + str(matriz[i][j])
        print(saida)

#t = '''010
#       111
#       000
#       101'''

#t = '''10101
#       10101
#       11111'''

t = '''0011001010
       0110001010
       0011001110
       0000000000
       0010001010
       0010011111
       1111100000
       0010001110
       0010001110'''

matriz = geraMatriz(t)

def verificaVizinho(i, j, cont):
    if(matriz[i][j] != 999):
        return()
    matriz[i][j] = cont

    if(len(matriz[i]) > j + 1):
        verificaVizinho(i, j + 1, cont)
    if(len(matriz) > i + 1):
        verificaVizinho(i + 1, j, cont)
    if(j - 1 >= 0):
        verificaVizinho(i, j - 1, cont)
    if(i - 1 >= 0):
        verificaVizinho(i - 1, j, cont)
    return()

print('Entrada:')
imprimiMatriz(matriz)

for i in range(len(matriz)): #linha
    for j in range(len(matriz[i])): #coluna
        if(matriz[i][j] == 1):
            matriz[i][j] = 999

cont = 1

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        verificaVizinho( i,j, cont)
        if (matriz[i][j] == cont):
            cont += 1

print('Saída:')
imprimiMatriz(matriz)