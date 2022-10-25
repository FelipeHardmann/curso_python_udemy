from random import randint

def geraMatricula(tamanho: int) -> int:
    return int(''.join([str(randint(1, 9)) for _ in range(tamanho)]))


class Aluno:

    def __init__(self, nome: str, cpf: str, email: str):
        self.matricula = geraMatricula(5)
        self.nome = nome
        self.cpf = cpf
        self.email = email
    