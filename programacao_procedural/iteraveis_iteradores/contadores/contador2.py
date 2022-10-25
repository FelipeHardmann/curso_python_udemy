'''
Combinations, Permutation e Product - Itertools
Combinação - Ordem ñ importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produtos - Ordem importa e repete valores únicos
'''
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia'' Fabricio', 'Rose']

for grupo in combinations(pessoas, 2):
    print(grupo)

print('#'*20)

for grupo in permutations(pessoas, 2):
    print(grupo)

print('#'*20)

for grupo in product(pessoas, repeat = 2):
    print(grupo)