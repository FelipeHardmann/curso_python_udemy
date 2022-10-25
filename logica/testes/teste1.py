num = input('Digite um número inteiro: ')

if num.isdigit(): # Pergunta se o número é inteiro ou não
    num = int(num)

    if num % 2 == 0:
        print(f'Número {num} é par')
    else:
        print(f'Número {num} é ímpar')
else:
    print('Esse número não é inteiro')

