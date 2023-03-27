from models import *

# cp1 = ContaPoupanca(111, 222, 0)
# cp1.depositar(1)
# print(cp1.sacar(1))

cc1 = ContaCorrente(111, 222, 0,100)
print(cc1.sacar(101))

cliente = Cliente('Felipe', 22)
cliente.conta = ContaPoupanca(111, 111, 2000)
print(cliente)
print(cliente.conta)
