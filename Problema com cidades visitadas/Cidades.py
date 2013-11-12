# -*- coding: utf-8 -*-
# Utlização de uma matriz de números, onde verificará e imprimirá regiões existentes
# Apenas verificará os 1(s) que estão somente na horizontal e vertical

matriz = [[0,1,0,0,0,0],
          [0,0,1,0,0,0],
          [0,0,0,0,1,0],
          [0,0,1,0,1,0],
          [1,0,0,0,0,0],
          [0,1,0,0,0,0]]

'''[[0,1,0],
	    [1,1,1],
        [0,0,0],
	    [1,0,1]

[[0,1,1,0,0,0,1,0,1,0],
[0,0,1,1,0,0,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,1,0,1,0],
[0,0,1,0,0,1,1,1,1,1],
[1,1,1,1,1,0,0,0,0,0],
[0,0,1,0,0,0,1,1,1,0],
[0,0,1,0,0,0,1,1,1,0],
[0,0,1,1,1,0,0,0,1,0]]'''

def varre( i, j, cont ):
    if( matriz[i][j] != 999 ):#Se for 0 faz nada
        return()
    matriz[i][j] = cont# Troca 999 pelo valor de cont

    #Aqui está verificando se pode varrer o elemento

    if( len( matriz[i] ) > j + 1 ):    # da direita  
        varre( i, j + 1, cont )                   
    if( len( matriz ) > i + 1 ):       #de cima
        varre( i + 1, j, cont )
    if( j - 1 >= 0 ):                  #da esquerda
        varre( i, j - 1, cont )
    if( i - 1 >= 0 ):                  #o debaixo
        varre( i - 1, j, cont )
    return()

#Percorre cada elemento da matriz e subistitui por 999
for i in range( len( matriz ) ): #linha
    for j in range( len( matriz[i] ) ): #coluna
        if( matriz[i][j] == 1 ):
            matriz[i][j] = 999

cont = 1
# Varrerá a matriz, chamando a funçao de troca para cd posiçao com 999
for i in range( len( matriz ) ):
    for j in range( len( matriz[i] ) ):
        varre( i,j, cont)
        if ( matriz[i][j] == cont ):
            cont += 1

# aqui se encarregará de mostrar as regiões, com sua devidas regiões
print( "\nMatriz depois: ")
for i in range( len( matriz ) ):#laço que imprimirá a matriz formatada (depois)
    matrix = ''
    for j in range( len( matriz[i] ) ):
        matrix = matrix + str( matriz[i][j] ) + ' '
    print( matrix )
