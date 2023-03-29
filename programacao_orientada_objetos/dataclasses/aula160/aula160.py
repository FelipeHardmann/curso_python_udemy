# As dataclass geram sozinhas os getters e os setters em python
# Além de gerar também o repr
# Além de gerar o método __eq__ e __init__

from dataclasses import dataclass, asdict


'''
    Podemos desativar o __init__ padrão da dataclass
    com init=False, além disso, colocar o atributo frozen
    que deixa proíbido a forma de atribuição
'''
@dataclass(frozen=True)
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        '''
            O post_init é executado logo após o init da dataclass
            ele tem 
        '''
        self.nome_completo = f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Felipe', 'Hardmann')
# p1.nome = 'Adriano'
print(p1.nome_completo)
print(asdict(p1))
