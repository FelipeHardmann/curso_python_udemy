'''
Funções (def) em python - *args **kwargs -
Parte 3
'''

#**kwargs são argumentos com palavra chave

def func(*args): #Args é basicamente um empacotamento e desempacotamento
    for v in args:
        print(v)
    '''args = list(args) #Transformando em Lista
    args[0] = 20
    print(args)'''
'''    print(args[0])
    print(args[-1])
    print(len(args))'''

func(1, 2, 3, 4, 5)

'''lista = [1, 2, 3, 4, 5]
print(*lista, sep='-') #Desempacotando Lista'''