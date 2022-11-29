class Carro:
    # Inicializador
    def __init__(self, nome):
        self.nome = nome

    # Métodos
    def acelarar(self):
        print(f'{self.nome} está acelerando')

    def parar(self):
        print(f'{self.nome} está parado')


fusca = Carro('Fusca')
print(fusca.acelarar())
print(fusca.parar())
print(fusca.nome)