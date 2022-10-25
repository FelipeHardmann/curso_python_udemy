import math

PI = math.pi

def dobraLista(lista):
    return [x*2 for x in lista]

def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

lista = [1, 2, 3, 4, 5]

if __name__ == '__main__': #Aqui você usa para que todas essas funções não sejam executadas no outro modulo
    print(dobraLista(lista))
    print(multiplica(lista))
    print(PI)
