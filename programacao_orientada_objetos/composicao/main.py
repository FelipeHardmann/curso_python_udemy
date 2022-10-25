from classes import Cliente, Endereco

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Felipe', 22)
cliente2.insere_endereco('Salvador', 'BA')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('João', 10)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
print()

print('#'*50)

print()