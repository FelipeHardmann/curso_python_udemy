'''lista = ['Hello World', 'Tchau mundo', 'Olá mundo']
lista = [ ' '.join(txt.split(' ')[::-1]) for txt in lista]
print(lista)'''

'''original_list = [2,3.75,.04,59.354,6,7.7777,8,9]
only_ints = [number for number in original_list if type(number) == int]
print(only_ints)
'''
'''def converteNumero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

def contNum(number):
    lista = []
    for i in range(1, number + 1):
        lista.append(i)
        print(lista)
        
        
num = converteNumero(input('Digite um número: '))
contNum(num)'''

# lista = [item**2 for item in range(10)]

# resultado = [str(item).upper() for item in lista]

print('''
    ========== MENU ==========

        1 - bLA BLA 
        
''')