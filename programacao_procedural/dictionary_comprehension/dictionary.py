'''
Além da compreensão de listas e dicionário você pode fazer de conjuntos também
'''

lista =[
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

d1 = {x: y for x, y in lista} #Isso é igual a função dict()
print(d1)