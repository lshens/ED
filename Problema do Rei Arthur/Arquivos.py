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
        #print("Original: %s" % txt[aux_d])
        aux_lst = txt[aux_d].split()
        pessoa = str(aux_lst[:1:])
        pessoa.find("[")
        preferidos = aux_lst[1::]
        dic.update({pessoa: preferidos})
        aux_d += 1
        #print(dic.keys())
    #te = dic.keys()
    #te2 = te[:1:]
    #te3 = ["['Renata']"]
    #print (te2 == te3)
    #print(te2)
    #print(te3)
        #print("Damas: %s, seus preferidos: %s" % (pessoa, preferidos))

    #print(lst.values())


arquivo("C:\Users\Shen\PycharmProjects\ED\Problema do Rei Arthur\casamento.txt")