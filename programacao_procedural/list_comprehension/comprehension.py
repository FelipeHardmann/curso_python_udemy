'''
Otimização do código
'''

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1]

l3 = [v * 2 for v in l1]
l4 = [(v, v2) for v in l1 for v2 in range(3)]
print(l4)