'''
Composição é a relação mais forte entre classes
Uma classe vai ser dona de objetos de outra classe
Se a principal for apagada todos os objetos da outra classe serão apagados
'''

class Cliente:
    def __init__(self, nome, idade):
        '''Metodo construtor'''
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        '''Função para adicionar a cidade e o estado'''
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        '''Função para retornar uma lista de estados e cidades'''
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')


class Endereco:
    def __init__(self, cidade, estado):
        '''Método construtor de Endereço'''
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} foi apagado')