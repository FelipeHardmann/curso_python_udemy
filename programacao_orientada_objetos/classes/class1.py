'''
Classes podem atributos(características, dados dentro da classe) e métodos(Funções)
'''
# Por convenção, usamos PascalCase para nomes de classes
# Todo primeiro parametro precisa receber self

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


nome = input('Digite seu nome: ')
sobrenome = input('Sobrenome: ')


p1 = Pessoa(nome, sobrenome)
# p1.nome = 'Felipe'
# p1.sobrenome = 'Hardmann'
print(p1.nome, p1.sobrenome)
