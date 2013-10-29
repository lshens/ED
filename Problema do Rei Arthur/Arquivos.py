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
        damas = str(aux_lst[:1:])
        preferidos = aux_lst[1::]
        dic.update({damas: preferidos})
        aux_d += 1

        #print("Damas: %s, seus preferidos: %s" % (damas, preferidos))

    #print(lst.values())
    print(dic.items())


arquivo("d:\casamento.txt")