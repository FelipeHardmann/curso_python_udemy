'''def soma(n1, n2, n3):
    return n1 + n2 + n3

somaTotal = soma(2, 2, 2)
print(somaTotal)'''

def calculo(num1):
    if num1 % 3 == 0 and num1 % 5 == 0:
        return 'FizzBuzz'
    elif num1 % 2 == 0:
        return 'Fizz'
    elif num1 % 5 == 0:
        return 'Buzz'

fizzbuzz = calculo(25)
print(fizzbuzz)
