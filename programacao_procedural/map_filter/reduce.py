from dados import produtos, pessoas, lista
from functools import reduce

'''somaLista = reduce(lambda ac, i: i + ac, lista, 0)
print(somaLista)'''

'''somaPrecos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(somaPrecos)'''

somaIdades = reduce(lambda ac, pessoa: ac + pessoa['idade'], pessoas, 0)
print(round(somaIdades / len(pessoas)))