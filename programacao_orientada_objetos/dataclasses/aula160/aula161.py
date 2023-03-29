from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class Pessoa:
    nome: str
    sobrenome: str


p1 = Pessoa('Felipe', 'Hardmann')
# p1.nome = 'Adriano'
# print(p1.nome_completo)
print(asdict(p1))
