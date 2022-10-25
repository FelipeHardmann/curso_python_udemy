'''
Split, Join, Enumerate em Pyhton
* Split - Dividir uma String # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
'''

#Função do split
'''string = 'O Brasil é o páis do futebol, o Brasil é penta'
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase')#count função para fazer a contagem de Strings
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')'''

#Função Join
'''lista = ['O', 'Brasil', 'é', 'penta']
listaJoin = ','.join(lista)
print(listaJoin)'''

#Função enumerate - Retorna Tuplas
'''string = 'O Brasil é penta'
lista = string.split(' ')
for indice, valor in enumerate(lista):
    print(indice, valor)'''

lista = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for v in lista:
    print(v[0])