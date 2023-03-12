class Multiplicar:
    def __init__(self, multiplicador) -> None:
        self.multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * self.multiplicador
        return interna
    
@Multiplicar(2)
def soma(x, y):
    return x + y

teste = soma(2, 4)
print(teste)
