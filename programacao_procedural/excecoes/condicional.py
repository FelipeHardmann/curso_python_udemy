#Utlilzando try como condicional

def converteNumero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    num = converteNumero(input('Digite um número: '))

    if num is None:
        print('Erro: isso não é número')
    else:
        print(num * 5)
