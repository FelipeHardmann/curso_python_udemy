# Funções parte 4, escopo de variáveis

'''
Diferenciando as variáveis quando estão em escopo global e em funções
'''

variavel  = 'valor'
def func():
    print(variavel)

def func2():
    global variavel #A palavra reservada global é usada para deixar a variável acessível em todos os locais
    #Isso não é uma boa prática
    variavel = 'outro valor'
    print(variavel)

func()
func2()
print(variavel)