'''
Funções Lambda, funções que são anônimas
'''

'''def funcao(arg, arg2):
    return arg * arg2

var = funcao(2, 2)'''

#A de cima e a de baixo retornam a mesma coisa
'''a = lambda x, y: x * y 
print(a(2, 2))'''

#Outros exemplos usando Lambda
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8] 
]

'''def func(item):
    return item[1]'''

lista.sort(key = lambda item: item[1], reverse = True)
print(lista)