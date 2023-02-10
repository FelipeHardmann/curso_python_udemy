class Cachorro:
    def __init__(self, tamanho: float, peso: float, cor: str, nome: str, raca: str) -> None:
        self.tamanho = tamanho
        self.peso = peso
        self.cor = cor
        self.nome = nome
        self.raca = raca

    def latir(self):
        '''Método para latir'''
        print(f'{self.nome} está latindo')

    def rosnar(self):
        '''Método para rosnar'''
        print(f'{self.nome} está rosnando')

    def dormir(self):
        '''Método para dormir'''
        print(f'{self.nome} está dormindo')

    
cachorro = Cachorro(1.10, 20, 'Preto', 'Bob', 'Pitbull')
cachorro.latir()
cachorro.dormir()
cachorro.rosnar()
