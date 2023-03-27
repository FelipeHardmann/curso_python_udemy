from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float, limite: float) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhar(f'Saque de {valor}')
            return self.saldo
        return f'Não foi possível sacar o valor desejado seu limite é {-self.limite:.2f}\nSeu saldo é de {self.saldo}'
