import sys #Esse módulo serve para vc acessar em qual plataforma o Script está sendo executado
print(sys.platform)

'''
O Python já vem com muitos modulos(pacotes) imbutidos, por isso, muitas
vezes não há a necessidade de utilizar o import
'''

from random import randint

for i in range(10):
    print(randint(0, 10))

#Você pode utilizar o * depois do import para importar tudo dentro do módulo, porém não é uma boa prática