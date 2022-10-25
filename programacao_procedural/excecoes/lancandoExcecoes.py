def divide(n1, n2):
    try:
        return  n1 / n2
    except ZeroDivisionError as error:
        print(error)
        raise #Relançando a mesma exceção

try:
    print(divide(2, 0))
except ZeroDivisionError as erro:
    print(erro)