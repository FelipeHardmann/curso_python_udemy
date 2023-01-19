# __dict__ e vars para atributos de instância

class Pessoa:
    __ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return f'{Pessoa.__ano_atual - self.idade}'

p1 = Pessoa('Felipe', 22)
print(p1.__dict__)
print(vars(p1))

# A funçao vars retorna uma dicionário igual ao dict
