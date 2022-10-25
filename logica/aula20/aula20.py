'''
For / Else em Pyhthon
'''
variavel = ['Luiz Otavio', 'Joazinho', 'Maria']

comeco = False
for valor in variavel:
    if valor.lower().startswith('j'):
        comeco = True

if comeco:
    print('Existe uma palavra que começa com J')
else:
    print('Não existe uma palavra que começa com J')