'''Função len'''

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Nome invalido')
else:
    print('Você foi cadastrado')

str1 = input('Digite alguma coisa: ')
str2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitado foi: {len(str1) + len(str2)}')