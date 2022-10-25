hora = int(input('Digite a hora: '))
name = input('Digite seu nome: ')

if 0 <= hora <= 11:
    print(f'Bom dia {name}')
elif 12 <= hora <= 17:
    print(f'Boa tarde {name}')
else:
    print(f'Boa noite {name}')