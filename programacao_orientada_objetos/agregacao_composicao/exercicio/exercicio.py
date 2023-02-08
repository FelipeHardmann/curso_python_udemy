# 1 - Crie uma classe Carros
# 2 - Crie uma classe motor
# 3 - Crie uma classe fabricante
# 4 - Faça uma ligação entre o carro e o motor
# Obs: um motor pode ter varios carros e fabricantes
# 5 - faça uma ligação entre um carro e um fabricante
# Obs: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, moto e fabricante

class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
    

class Fabricante:
    def __init__(self, nome) -> None:
        self.nome = nome


class Motor:
    def __init__(self, nome) -> None:
        self.nome = nome


carro1 = Carro('Fusca')
motor = Motor('1.0')
fabricante = Fabricante('Volkswagen')
carro1.fabricante = fabricante
carro1.motor = motor
print(carro1.nome, carro1.fabricante.nome, carro1.motor.nome)


carro2 = Carro('Kwid')
motor2 = Motor('1.0')
fabricante2 = Fabricante('Renault')
carro2.fabricante = fabricante2
carro2.motor = motor2
print(carro2.nome, carro2.fabricante.nome, carro2.motor.nome)