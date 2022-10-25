'''
Add (adiciona), update (atualiza), clear, discard
inion | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
'''

#Os sets, diferente dos dicionários não possuem chaves
#Para se criar um set em branco é necessário colocar a função set()
#As vezes ele retorna valores fora de ordem
#Não aceitam elementos duplicados

'''s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.update('O')
print(s1)'''

'''s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 | s2 #Função para unir os dois elementos
print(s3)'''

l1 = ['Luiz', 'João', 'Maria']
l2 = ['João', 'Maria', 'Maria',
      'Luiz', 'Luiz', 'Luiz']

if set(l1) == set(l2):
    print('L1 = L2')
else:
    print('Não é igual')
