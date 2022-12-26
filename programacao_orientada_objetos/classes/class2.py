# Métodos em instâncias de classes em Python

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')

    def frear(self):
        print(f'{self.nome} está freando')


fusca = Carro('Fusca')
print(fusca.nome)
print(fusca.acelerar())
# print(fusca.frear())

celta = Carro('Celta')
print(celta.nome)
print(celta.acelerar())
# print(celta.frear())
