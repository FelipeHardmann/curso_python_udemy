'''file = open('abc.txt', 'w+') #w+ faz com que você possa ler e escrever em um arquivo
file.write('Linha1\n')
file.write('Linha2\n')
file.write('Linha3\n')

file.seek(0, 0)#Essa função serve para você conseguir dar o print no arquivo, lendo todas as linhas que foram escritas
print('Lendo linhas: ')
print(file.read())
print('#'*30)

file.seek(0, 0)
print(file.readline(), end='')#Aqui ele vai lendo linha por linha
print(file.readline(), end='')
print(file.readline(), end='')
print('#'*30)

file.seek(0, 0)
print(file.readlines())#Desta forma o print retorna uma lista
print('#'*30)

file.seek(0, 0)
for linha in file:
    print(linha, end='')

file.close()'''

'''
você pode tentar abrir pelo metódo de Try
'''

'''with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())

#desta forma não necessário fecchar o arquivo'''

import json
d1 = {
    'Pessoa1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa2': {
    'nome': 'Rose',
    'idade': 30,
    }
}

d1_json = json.dumps(d1)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

print(d1)

