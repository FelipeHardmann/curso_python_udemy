'''lista = [1, 2, 3, 4, 5]
lista = iter(lista)
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(hasattr(lista, '__next__'))'''

import sys
import time
'''lista = list(range(10))
print(sys.getsizeof(lista))#Dessa forma podemos ver o tamanho de valores utlizados na memória que está sendo usada'''

def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r

g = gera()

for v in g:
    print(v)

#Os geradores usam menos memória do que as listas
