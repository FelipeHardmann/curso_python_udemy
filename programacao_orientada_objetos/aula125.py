# Atributos de classe

class Pessoa:
    __ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return f'{Pessoa.__ano_atual - self.idade}'

p1 = Pessoa('Felipe', 22)
p2 = Pessoa('Natalia', 20)

# Se vc utilizar essa forma o seu ano atual ficará salvo
# como 1, porém, se vc utilizar o método privado, ele não
# alterará

Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
