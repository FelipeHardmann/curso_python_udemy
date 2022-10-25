'''
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

===================== resultado
lista_soma = [2, 4, 6, 8]
'''

#Minha solução
lista = [10, 20, 30, 40, 50]
lista2 = [60, 70, 80, 90, 100]

lista3 = zip(lista, lista2)
lista4 = []
for x in lista3:
    x = x[0] + x[1]
    lista4.append(x)
print(lista4)

#Outra solução

'''lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = []
for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)'''

#Solução Pythonica

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)