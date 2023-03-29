from models import Conta
from dataclasses import dataclass

class ContaCorrente(Conta):
    def __init_subclass__(cls, limite: float) -> None:
        return super().__init_subclass__()
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_max = -self.limite

        if valor_pos_saque >= limite_max:
            self.saldo -= valor
        