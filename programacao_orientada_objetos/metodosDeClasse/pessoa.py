class Pessoa:

    ano_atual = 2023

    def __init__(self,nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return f'{self.ano_atual - self.idade}'

    @classmethod
    def por_ano_nascimento(cls, nascimento, nome):
        idade = cls.ano_atual - nascimento
        return cls(nome, idade)


p1 = Pessoa('Felipe', 22)
p2 = Pessoa('Luiz', 19)
print(p1.get_ano_nascimento())