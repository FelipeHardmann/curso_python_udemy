# As dataclass geram sozinhas os getters e os setters em python
# Além de gerar também o repr
# Além de gerar o método __eq__ e __init__

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = sobrenome


p1 = Pessoa('Felipe', 'Hardmann')
p1.nome_completo = 'Felipe Adriano'
print(p1)
