# Funções decoradas em Python

class Time:
    def __init__(self, nome: str) -> None:
        self.nome = nome


class Planeta:
    def __init__(self, nome: str) -> None:
        self.nome = nome


brasil = Time('Brasil')
portugla = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')
