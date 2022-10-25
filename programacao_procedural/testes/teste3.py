carrinho = []

carrinho.append(('Produto1', 30))
carrinho.append(('Produto2', 20))
carrinho.append(('Produto3', 50))

'''total = 0

for produto in carrinho:
    total += produto[1]

print(total)'''

total = sum([float(y) for x, y in carrinho]) #Essa é a forma mais eficaz em Python
print(total)