'''Desafio'''

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, com {altura} de altura, {peso}Kg, nasceu no ano de {ano_nascimento}'
      f' e possui um IMC de {imc:.2f}')
