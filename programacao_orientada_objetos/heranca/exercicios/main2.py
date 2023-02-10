class Animal:
    def __init__(self, peso: float, idade: int, membros: int) -> None:
        self._peso = peso
        self._idade = idade
        self._membros = membros

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, valor):
        self._peso = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor

    @property 
    def membros(self):
        return self._membros

    @membros.setter
    def membros(self, valor):
        self._membros = valor

    def emitir_som(self):
        return 'Animal emitindo som'

    def comer(self):
        return 'Animal se alimentando'


class Mamifero(Animal):
    def __init__(self, peso: float, idade: int, membros: int, tem_pelo: bool, cor: str) -> None:
        super().__init__(peso, idade, membros)
        self._pelo = tem_pelo
        self._cor = cor if tem_pelo else None

    @property
    def pelo(self):
        return self._pelo

    @pelo.setter
    def pelo(self, valor):
        self._pelo = valor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor

mamifero = Mamifero(71, 20, 4, True, 'Rosa')
print(mamifero.__dict__)
