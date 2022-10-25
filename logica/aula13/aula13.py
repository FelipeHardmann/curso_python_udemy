'''

Formantando valores com modificadores

:s - Texto
:d - Inteiros
:f - Números de pontos flutuantes
:.(NÚMERO)f - Quantidae de casas decimais
:(CARACTERE) (> ou < ou ^) (quantidade) (TIPO - s, d ou f)

> - Esquerda - coloca a variável a esquerda
< - Direita - Coloca a variável a direita
^ - Centro - Coloca a variável no centro
'''
num1 = 10
num2 = 3
divisao = num1 / num2
print(f'{divisao:.2f}')
print(f'{divisao:#^50.2f}')