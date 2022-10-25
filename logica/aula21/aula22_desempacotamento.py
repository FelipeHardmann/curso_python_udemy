'''
Desempacotamento de listas em Python
'''

lista = ['Luiz', 'João', 'Maria']
n1, n2, n3 = lista #Desempacotamento padrão

*_, l1, l2, l3 = lista
print(l1, l2, l3)
