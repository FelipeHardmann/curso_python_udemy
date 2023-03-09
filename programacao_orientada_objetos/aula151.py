# Funções decoradas em Python
def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        if 'Terra' in resultado:
            return 'Você está em casa'
        return resultado
    return interno


class SuperTime:
    ...

@adiciona_repr
class Time:
    def __init__(self, nome: str) -> None:
        self.nome = nome

@adiciona_repr
class Planeta:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    @meu_planeta
    def falar_nome(self) -> str:
        return f'O planeta é {self.nome}'


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(marte)
print(terra)

print(terra.falar_nome())
print(marte.falar_nome())
