"""class A:
    def falar(self):
        print('Falando... Estou em A.')


class B(A):
    def falar(self):
        print('Falando... Estou em B.')


class C(A):
    def falar(self):
        print('Falando... Estou em C.')

# A classe D tem tudo que tem B e C
# A classe começa a procurar o método da esquerda para direita
# Então se existir métodos com o mesmo nome ele vai escolher o primeiro.
class D(B, C):
    pass


'''
Um sistema pode ficar muito complexo se tiver muita herança
'''"""

from smartphone import Smartphone


smartphone = Smartphone('Iphone')
smartphone.conectar()
smartphone.desligar()
smartphone.ligar()
smartphone.conectar()
smartphone.conectar()
smartphone.conectar()
smartphone.desligar()
smartphone.conectar()
smartphone.desconectar()