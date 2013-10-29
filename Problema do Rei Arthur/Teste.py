# -*- coding: utf-8 -*-
import copy

guyprefers = {
 'abe':  ['abi', 'eve', 'cath', 'ivy', 'jan', 'dee', 'fay', 'bea', 'hope', 'gay'],
 'bob':  ['cath', 'hope', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'gay'],
 'col':  ['hope', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'gay', 'cath', 'jan'],
 'dan':  ['ivy', 'fay', 'dee', 'gay', 'hope', 'eve', 'jan', 'bea', 'cath', 'abi'],
 'ed':   ['jan', 'dee', 'bea', 'cath', 'fay', 'eve', 'abi', 'ivy', 'hope', 'gay'],
 'fred': ['bea', 'abi', 'dee', 'gay', 'eve', 'ivy', 'cath', 'jan', 'hope', 'fay'],
 'gav':  ['gay', 'eve', 'ivy', 'bea', 'cath', 'abi', 'dee', 'hope', 'jan', 'fay'],
 'hal':  ['abi', 'eve', 'hope', 'fay', 'ivy', 'cath', 'jan', 'bea', 'gay', 'dee'],
 'ian':  ['hope', 'cath', 'dee', 'gay', 'bea', 'abi', 'fay', 'ivy', 'jan', 'eve'],
 'jon':  ['abi', 'fay', 'jan', 'gay', 'eve', 'bea', 'dee', 'cath', 'ivy', 'hope']}
galprefers = {
 'abi':  ['bob', 'fred', 'jon', 'gav', 'ian', 'abe', 'dan', 'ed', 'col', 'hal'],
 'bea':  ['bob', 'abe', 'col', 'fred', 'gav', 'dan', 'ian', 'ed', 'jon', 'hal'],
 'cath': ['fred', 'bob', 'ed', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon'],
 'dee':  ['fred', 'jon', 'col', 'abe', 'ian', 'hal', 'gav', 'dan', 'bob', 'ed'],
 'eve':  ['jon', 'hal', 'fred', 'dan', 'abe', 'gav', 'col', 'ed', 'ian', 'bob'],
 'fay':  ['bob', 'abe', 'ed', 'ian', 'jon', 'dan', 'fred', 'gav', 'col', 'hal'],
 'gay':  ['jon', 'gav', 'hal', 'fred', 'bob', 'abe', 'col', 'ed', 'dan', 'ian'],
 'hope': ['gav', 'jon', 'bob', 'abe', 'ian', 'dan', 'hal', 'ed', 'col', 'fred'],
 'ivy':  ['ian', 'col', 'hal', 'gav', 'fred', 'bob', 'abe', 'ed', 'jon', 'dan'],
 'jan':  ['ed', 'hal', 'gav', 'abe', 'bob', 'jon', 'col', 'ian', 'fred', 'dan']}

cavaleiros = sorted(guyprefers.keys())
mocas = sorted(galprefers.keys())


def check(engaged):
    inverseengaged = dict((v,k) for k,v in engaged.items())
    for she, he in engaged.items():
        shelikes = galprefers[she]
        shelikesbetter = shelikes[:shelikes.index(he)]
        helikes = guyprefers[he]
        helikesbetter = helikes[:helikes.index(she)]
        for guy in shelikesbetter:
            guysgirl = inverseengaged[guy]
            guylikes = guyprefers[guy]
            if guylikes.index(guysgirl) > guylikes.index(she):
                print("%s e %s gostam um do outro melhor que"
                      "o casal atual: %s e %s, respectivamente"
                      % (she, guy, he, guysgirl))
                return False
        for gal in helikesbetter:
            girlsguy = engaged[gal]
            gallikes = galprefers[gal]
            if gallikes.index(girlsguy) > gallikes.index(he):
                print("%s e %s gostam um do outro melhor que"
                      "o casal atual: %s e %s, respectivamente"
                      % (he, gal, she, girlsguy))
                return False
    return True

def matchmaker():
    guysfree = cavaleiros[:]
    engaged  = {}
    guyprefers2 = copy.deepcopy(guyprefers)
    galprefers2 = copy.deepcopy(galprefers)
    while guysfree:
        cavaleiros = guysfree.pop(0)
        guyslist = guyprefers2[cavaleiros]
        gal = guyslist.pop(0)
        fiance = engaged.get(gal)
        if not fiance:
            # Esta solteira
            engaged[gal] = cavaleiros
            print("  %s and %s" % (cavaleiros, gal))
        else:
            # O caipira propõe uma moça envolvida
            galslist = galprefers2[gal]
            if galslist.index(fiance) > galslist.index(cavaleiros):
                # ela prefere o novo cara
                engaged[gal] = cavaleiros
                print("  %s dumped %s for %s" % (gal, fiance, cavaleiros))
                if guyprefers2[fiance]:
                    # Ex has more girls to try
                    guysfree.append(fiance)
            else:
                # She is faithful to old fiance
                if guyslist:
                    # Look again
                    guysfree.append(cavaleiros)
    return engaged


print('\nCasados:')
comprometido = matchmaker()

print('\nCasais:')
print('  ' + ',\n  '.join('%s é formou casal com %s' % casal
                          for casal in sorted(comprometido.items())))
print()
print('Verificação da estabilidade de noivado PASSOU'
      if check(comprometido) else 'Verificação da estabilidade de noivado FALHO')

print('\n\nTroca de dois noivos a introduziu ao ERRO')
comprometido[mocas[0]], comprometido[mocas[1]] = comprometido[mocas[1]], comprometido[mocas[0]]
for moca in mocas[:2]:
    print('  %s agora está comprometido com' % (moca, comprometido[moca]))
print()
print('Verificação da estabilidade de noivado PASSOU'
      if check(comprometido) else 'Verificação da estabilidade de noivado FALHOU')
