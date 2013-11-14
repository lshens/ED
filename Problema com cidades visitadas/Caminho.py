# -*- coding: utf-8 -*-



def percorre(matriz):
    #A matriz é varrida de cima(linha[0]) para baixo(linha[n]) e
    #da esquerda(coluna[0] para a direita[n]
    aux = []
    cont = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
          #  print(matriz[linha][coluna])
            #Se um "pixel" tem valor 1, verificamos seu vizinho de cima e da esquerda
            if '1' in matriz[linha][coluna]:
                #Se ambos são ZERO, um novo objeto começa neste pixel(Um novo regioes)
                if matriz[linha -1][coluna] and matriz[linha][coluna - 1] == '0':
                    aux.append(matriz[linha][coluna])
                #Se um deles é 1, este pixel pertence ao objeto anterior
                if matriz[linha -1][coluna] == '1' or matriz[linha][coluna - 1] == '1':
                    aux.extend(matriz[linha][coluna])
            else:
                aux.append(matriz[linha][coluna])
            #Se ambos os vizinhoes tem rotulos diferentes, a matriz devera ser corrigida para que
            #ambos tenham o mesmo rotulo ( ou seja, um dos rotulos vai desaparecer e todos os pixels daquele
            #rotulo vão passar a ter outro)
    print(aux)



t = '''010
       111
       000
       101'''

#print("Entrada:")
#imprimiMatriz(geraMatriz(t))

percorre(geraMatriz(t))


