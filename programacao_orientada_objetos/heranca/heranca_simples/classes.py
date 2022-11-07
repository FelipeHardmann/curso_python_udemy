class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print('Falando')


# Aqui é fazendo a hrança
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} Comprando....')


class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando')



##########################Anotações################################
'''
Tudo que tem em Pessoa tem em Cliente, mas Pessoa não herda nada de Cliente
E tudo que tem em ClienteVip tem em Cliente, Cliente e ClienteVip são uma Pessoa, mas,
nem toda pessoa é um cliente
'''