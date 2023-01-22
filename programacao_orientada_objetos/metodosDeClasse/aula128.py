# Métodos de de classe
# São métodos onde self será "cls", ou seja, não contará o o self
# não receberá uma instância para classe 

class Pessoa:
    ano = 2023

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_classe(cls):
        print('Olá')

    @classmethod
    def criar_50_anos(cls, nome):
        return cls(nome, 50)

#  Os métodos de classes não exigem  que se passe algum parametro na função 
# p1 = Pessoa()
p2 = Pessoa.criar_50_anos('Felipe')
print(p2.nome, p2.idade, sep=' --- ')
 
     