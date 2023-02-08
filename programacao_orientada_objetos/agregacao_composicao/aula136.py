class Cliente:
    def __init__(self, nome) -> None:
        self.nome= nome
        self.endercos = []

    def inserir(self, rua, numero):
        self.endercos.append(Enderco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.endercos.append(endereco)

    def listar(self):
        for endereco in self.endercos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('Apagando', self.nome)


class Enderco:
    def __init__(self, rua, numero) -> None:
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('Apagando', self.rua, self.numero)


cliente = Cliente('Maria')
cliente.inserir('Av.Brasil', 123)
cliente.inserir('Av.Stella', 321) 
endereco_externo = Enderco('Av.Saudade', 1234)
cliente.listar()
