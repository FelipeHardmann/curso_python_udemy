'''d1 = {
    'chave1': 'valor da chave'
}
d1['nova_chave'] = 'Valor da nova chave' '''#Aqui está criando uma nova chave com novo valor
#Pode ser usado a função update
#Pode transformar listas e Tuplas em dicionário 


'''d1 = dict(chave1 = 'Valor da chave', chave2 = 'Valor da outra chave')
d1['nova_chave'] = 'valor da nova chave'

dic = {
    'nome': 'Felipe' 'Adriano',
    'idade' : 22
}

print(dic.get())'''


clientes = {
    'cliente1': {
        'nome': 'Felipe',
        'sobrenome': 'Hardmann'
    },
    'cliente2': {
        'nome': 'Luiz',
        'sobrenome': 'Otavio'
    }
}

for cliente_k, cliente_v in clientes.items():
    print(f'Exibindo {cliente_k}')
    for dados_k, dados_v in clientes.items():
        print(f'\t{dados_k} = {dados_v}')














