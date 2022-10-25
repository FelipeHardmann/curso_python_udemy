'''
count - itertools: te gera um contador que é um iterador
'''

'''from types import GeneratorType

variavel = ((x, y) for x, y in zip('Alo', 'alo'))
print(list(variavel))'''

from itertools import count

contador = count(start = 5, step = 2)#Posso colocar o valor que eu quero que ele comece
#Vai contando de 1 em 1
#Ele precisa de atenção, pois pode gerar um looping infinito, necessário usar o break para poder parar o looping
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
