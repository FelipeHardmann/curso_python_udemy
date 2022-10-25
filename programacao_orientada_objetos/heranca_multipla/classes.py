class A:
    def falar(self):
        print('Falando... Estou em A.')


class B(A):
    def falar(self):
        print('Falando... Estou em B.')


class C(A):
    def falar(self):
        print('Falando... Estou em C.')

# A classe D tem tudo que tem B e C
class D(B, C):
    pass


'''
Um sistema pode ficar muito complexo se tiver muita herança
'''