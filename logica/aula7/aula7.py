'''Formatação de strings'''

'''
Aula sobre variáveis - apelido para algo que guarde algo na memória do computador
'''

nome = 'Luiz'
idade = 32
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)

'''Comando f antes das "" '''
print(f'Nome: {nome}')
print(f'Idade {idade}')
print(f'Altura: {altura}')
print(f'É maior: {e_maior} e o IMC é: {imc:.2f}')