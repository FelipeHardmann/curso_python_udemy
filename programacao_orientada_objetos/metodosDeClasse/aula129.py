# @statimethod (métodos estáticos) são inúteis
# Métodos estáticos são métodos que estão dentro da classe
# mas não tem acesso ao self nem ao cls.
# em resumo, são funções que existem dentro da sua classe

class Classe:
    @staticmethod
    def function(*args, **kwargs):
        print('Oi', args, kwargs)

def funcao(*args, **kwargs):
    print('Oi', args, kwargs)


c1 = Classe()
c1.function(1, 2, 3)
funcao(1, 2, 3)
Classe.function(nomeado=1)
funcao(nomeado=1)
