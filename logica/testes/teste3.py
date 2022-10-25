name = input('Digite seu nome: ')
qnt_letras = len(name)

if qnt_letras <= 4:
    print('Seu nome é curto')
elif 5 <= qnt_letras <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande!')