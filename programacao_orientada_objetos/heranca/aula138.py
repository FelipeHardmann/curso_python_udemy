# Herança uma relação entre classes
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# Ter cuidado com a parte de herança, não deixar muito complexo, no máximo 3 níveis

class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def fala_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    ...


c1 = Cliente('Felipe', 'Adriano')
c1.fala_nome_classe()
a1 = Aluno('Maria', 'Helena')
a1.fala_nome_classe()