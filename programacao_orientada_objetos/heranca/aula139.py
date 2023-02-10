# super() é uma super classe na sub classe
# Classe Principal (Pessoa)
#   -> super class, base class, parent class
# Classes filas (Cliente)
#   -> sub class, child class, derived class


class A:
    atributo_a = 'A'

    def __init__(self, atributo) -> None:
        self.atributo = atributo

    def metodo(self):
        print('A')

    
class B(A):
    atributo_b = 'B'

    def __init__(self, atributo, outra_coisa) -> None:
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'C'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def metodo(self):
        A.metodo(self)
        B.metodo(self)
        print('C')


c = C('Atributo', 'Qualquer')

c.metodo()
        