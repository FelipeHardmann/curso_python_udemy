#O que é setter = Set(Ou seja configurar um valor, atribuindo um valor)
#Getter = Get(Obter um valor, basicamente ler o valor)

class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


p1 = Pessoa('Felipe')
print(p1.nome) #Quando é adicionado o property ele não precisa ser executado como método
#pois ele está se comportando como um atributo

'''
Não se pode ter setter sem gatter, mas pode ao contrário
'''