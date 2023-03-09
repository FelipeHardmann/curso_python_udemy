'''
Importante quando tivermos um código cheios de classes e métodos, para criarmos de forma  mais rápida as representações
das classes
'''
def meu_repr(self) -> str:
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


@adiciona_repr
class Carro:
    def __init__(self, marca: str, ano: int, nome: str) -> None:
        self.marca = marca
        self.ano = ano
        self.nome = nome


carro1 = Carro('Toyota', 2022, 'Camaro')
carro2 = Carro('Toyota', 2022, 'Camaro')
print(carro1, carro2)
