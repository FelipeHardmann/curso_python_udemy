# @property - um getter no modo Pythônico
# getter - um método para se obter um atributo
# cor -> get_cor() 
# modo pythônico
# @property uma propriedade do objeto 
# ela é um método que se comporta como atributo
# Geralmente é usada nas seguintes situações:
# - como getter 
# - p/ evitar quebrar código do cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo 


class Caneta:
    def __init__(self, cor) -> None:
        self._cor = cor

    @property
    def cor(self):
        return self._cor

    @property
    def cor_tampa(self):
        return 123


caneta = Caneta('Red')
print(caneta.cor)
print(caneta.cor_tampa)


# class Caneta:
#     def __init__(self, cor) -> None:
#         self._cor = cor

#     def get_cor(self):
#         return self.cor

    
# caneta = Caneta('Red')
# print(caneta.get_cor())
