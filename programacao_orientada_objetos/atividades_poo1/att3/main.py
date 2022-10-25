from contaCorrente import Conta

conta1 = Conta('Felipe Hardmann')
conta1.despositar(10000)
conta1.sacar_dinheiro(1000)
print(conta1.consultar_saldo())
print(conta1.sacar_dinheiro(1000))
print(conta1.consultar_saldo())