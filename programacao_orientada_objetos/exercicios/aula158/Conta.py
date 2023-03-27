from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self):
        ...
    
    def depositar(self, valor):
        self.saldo += valor
        self.detalhar(f'Deposito de {valor}')

    def detalhar(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} ({msg})')
    