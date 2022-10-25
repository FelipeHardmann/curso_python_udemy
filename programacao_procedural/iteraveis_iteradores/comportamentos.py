#Esse tipo de dado é sequência, ou seja, é interável
nome = 'Felipe'
iterador = iter(nome)
print(next(iterador))

#Essas duas formas são iguais

'''for letra in nome:
    print(letra)

print('-' * 80)

for letra in nome:
    print(letra)'''