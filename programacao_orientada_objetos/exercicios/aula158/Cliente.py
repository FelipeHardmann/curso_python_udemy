from Pessoa import Pessoa
from models import *


class Cliente(Pessoa):
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)
        self.conta: Conta | None = None

