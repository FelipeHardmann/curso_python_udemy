class Ponto:
    def __init__(self, x: int, y: int, z = 'String') -> None:
        self.x = x
        self.y = y
        self.z = z

    # Forma mais informal
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    # __repr__ é mais para desenvolvedores
    def __repr__(self) -> repr:
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'
        #  !r retorna a representação daquele objeto

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other


if __name__ == '__main__':
    p1 = Ponto(1, 2)
    p2 = Ponto(900, 800)
    p3 = p1 + p2
    print(p3)
    print(f'P1 é maior que P2? {p1 > p2}')
    print(f'P2 é maior que P1? {p2 > p1}')
    # print(ponto1)
    # print(repr(ponto2))
    # print(f'{ponto2!r}')    

