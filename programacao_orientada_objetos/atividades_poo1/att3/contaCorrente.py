from random import randint

def gera_numero_conta(tamanho: int) -> int:
  return int(''.join([ str(randint(0, 9)) for _ in range(tamanho)]))

class Conta:

    def __init__(self, nome: str) -> None:
        self.numero: int = gera_numero_conta(7)
        self.nome: str = nome
        self.saldo: float = 0

    def consultar_saldo(self):
        return f'A conta {self.numero} possui um saldo de {self.saldo}'

    def sacar_dinheiro(self, valor: float):
        if self.saldo - valor >= 0:
            self.saldo -= valor
            return f'Saque realizado com sucesso, saque de R${valor:.2f}'
        else:
            return f'Saque indisponível por não possui limite, {self.saldo}, este é seu saldo'

    def despositar(self, valor: float):
        self.saldo += valor
        return f'Deposito de {valor} efetuado'

            