'''def saudacao(saudacao, nome):
    print(f'{saudacao} {nome}')  #Questão 1
saudacao('Olá', 'Felipe')'''

'''def soma(n1, n2, n3):
    print(n1 + n2 + n3)
soma(2, 3, 4)'''

'''def percentual(n1, percent):
    print(n1 + (n1 * percent / 100))
percentual(50, 10)
percentual(100, 10)'''

def fizzBuzz(n1):
    if n1 % 3 == 0 and n1 % 5 == 0:
        return 'FizzBuzz'
    elif n1 % 3 == 0:
        return 'Fizz'
    elif n1 % 5 == 0:
        return 'Buzz'

print(fizzBuzz(9))
print(fizzBuzz(15))
print(fizzBuzz(5))
