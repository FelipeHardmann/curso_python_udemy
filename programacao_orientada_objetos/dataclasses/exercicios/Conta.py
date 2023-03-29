from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Conta(ABC):
    agencia: int
    conta: int
    saldo: float

    @abstractmethod
    def sacar(self):
        ...
    
    def depositar(self, valor):
        self.saldo += valor
        self.detalhar(f'Deposito de {valor}')

    def detalhar(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} ({msg})')    