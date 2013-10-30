def arquivo(url):
    """

    :param url:
    """
    arq = open(url)
    txt = arq.readlines()
    aux_d = 0

    dic = {}
    for i in txt:


        linha = txt[aux_d].split()
        dic[linha[0]] = linha[1:]
        aux_d += 1
    arq.close()
    print(dic)
    #te = dic.keys()
    #te2 = te[:1:]
    #te3 = ["['Renata']"]
    #print (te2 == te3)
    #print(te2)
    #print(te3)
        #print("Damas: %s, seus preferidos: %s" % (pessoa, preferidos))

    #print(lst.values())


arquivo("C:\Users\lucas.shen\PycharmProjects\EstruturaDados\Problema do Rei Arthur\casamento.txt")