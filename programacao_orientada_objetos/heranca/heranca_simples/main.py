from classes import *

'''
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É 
'''
c1 = Cliente('Felipe', 22)
print(c1.nome)
c1.falar()
c1.comprar

print()

c2 = ClienteVip('Rose', 25, 'Maria')
c2.falar()


# a1 = Aluno('Adriano', 22)
# a1.falar()
# a1.estudar()