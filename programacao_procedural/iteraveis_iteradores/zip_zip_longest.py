'''
Zip - Unindo iteráveis
zip_longest - Itertools
'''
from itertools import zip_longest, count

indice = count(1)
cidades =['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidade_estado = zip(
    indice,
    estados,
    cidades
)

for indice, estados, cidades in cidade_estado:
    print(indice, estados, cidades)

#print(list(cidade_estado))

'''cidade_estado = zip(cidades, estados) -> dessa maneira ele elimina o resto da lista que não tiver chave

for valor in cidade_estado:
    print(valor)'''


