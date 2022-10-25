from dados import produtos, pessoas, lista

def filtra(produto):
    if produto['preco'] > 50:
        return True
    else:
        return False

#nova_lista = [x for x in lista if x > 5]
novaLista = filter(filtra, produtos) #Utilizada para filtrar valores que eu preciso ou quero

for produto in novaLista:
    print(produto)

print('#'*50)

def filtrarIdade(pessoa):
    if pessoa['idade'] >= 48:
        return True
    else:
        return False

listaPessoa = filter(filtrarIdade, pessoas)
for idade in listaPessoa:
    print(idade)
