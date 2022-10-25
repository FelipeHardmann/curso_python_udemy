from dados import produtos, pessoas, lista

'''novaLista = map_filter(lambda x: x * 2, lista)#O map_filter não retorna a lista, e sim o número de memória
nova_lista = [x * 2 for x in lista]#Pode se fzr em forma de listcomprehension
print(list(novaLista))#Para retornar em forma de lista é necessário mudar o type para list
print(nova_lista)'''

'''def aumentar(produto):
    produto['preco'] = round(produto['preco'] * 1.05, 2)
    return produto


novosProdutos = map_filter(aumentar, produtos) #Desta forma você está pegando o preco ou seja o value do dict

for produto in novosProdutos:
    print(produto)
'''

nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)

