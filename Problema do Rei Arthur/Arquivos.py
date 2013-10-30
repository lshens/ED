def arquivo(url):
    """

    :param url:
    """
    arq = open(url)
    txt = arq.readlines()
    aux_d = 0

    aux_lst = []
    dic = {}
    for i in txt:
        #pessoa = str(aux_lst[:1:])
        #preferidos = aux_lst[1::]
        aux_lst = txt[aux_d].split()
        dic.update({aux_d: aux_lst})
        aux_d += 1
    print(dic[0])
    #te = dic.keys()
    #te2 = te[:1:]
    #te3 = ["['Renata']"]
    #print (te2 == te3)
    #print(te2)
    #print(te3)
        #print("Damas: %s, seus preferidos: %s" % (pessoa, preferidos))

    #print(lst.values())


arquivo("C:\Users\Shen\PycharmProjects\ED\Problema do Rei Arthur\casamento.txt")