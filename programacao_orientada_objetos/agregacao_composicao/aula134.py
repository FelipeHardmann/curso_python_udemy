class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, valor_ferramenta):
        self._ferramenta = valor_ferramenta


class Ferramenta:
    def __init__(self, nome) -> None:
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


e = Escritor('Felipe')
caneta = Ferramenta('Bic')
e.ferramenta = caneta
print(caneta.escrever())
print(e.ferramenta.escrever())