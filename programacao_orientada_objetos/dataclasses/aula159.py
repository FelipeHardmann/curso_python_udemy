# As dataclass geram sozinhas os getters e os setters em python
# Além de gerar também o repr
# Além de gerar o método __eq__

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

p1 = Pessoa('Felipe', 22)
