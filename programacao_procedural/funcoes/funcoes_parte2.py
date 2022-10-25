'''
Funções (def) em Python - return - parte 2
'''

'''def funcao(var):
    return var

variavel = funcao('Valor que eu quero')

if variavel: #O valor none é falso em Booleano
    print(variavel) #Valor padrão é None que representa o ñ valor
else:
    print('Nenhum valor')'''

def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2

divide = divisao(8, 0)
if divide:
    print(divide)
else:
    print('Conta Inválida')