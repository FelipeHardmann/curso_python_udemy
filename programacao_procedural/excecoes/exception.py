'''
Tratamento de exceções
'''

'''
Você pode colocar as exceções que podem causar erro no código
colocando as formas de erro e escolhendo o que irá aparecer para o usuário
'''

try:
    print(a)
except NameError as erro:
    print('erro do desenvolvedor fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    pass
finally:
    a = ''

print(a)