'''
while em python
utilizado para realizar ações enquanto
uma condição for verdadeira
'''

'''x = 0
while x < 10:
    if x == 3:
        x = x + 1
    print(x)
    x = x + 1
print('Acabou!')'''

x = 0

'''while x < 10:
    y = 0
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1
    x += 1
print('Acabou!')'''

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador(+/-/* ou /): ')

    if not num_1.isnumeric() and num_2.isnumeric():
        print('Você precisa digitar um número')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)





