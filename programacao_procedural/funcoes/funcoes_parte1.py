'''
Funções - def em Python (Parte 1)
'''

def saudacao(msg = 'Olá', nome = 'Usuário'):#Dentro dos () colocamos os parametros // O olá usuário é valor padrão
# se não for colocado nada
    nome = nome.replace('e', '3')#Modificando as palavras
    msg = msg.replace('e', '3')
    print(msg, nome) #Esse é o argumento que é um parametro // Normalmente ñ usamos o print e sim o return

saudacao('Olá', 'Felipe') #Aqui ele está passando o argumento que msg e nome irá receber
saudacao(nome = 'Zé', msg = 'Oi')#Dessa maneira podemos inverter a forma de quem aparecerá primeiro
saudacao('Olá', 'Felipe')
saudacao('Olá', 'Felipe')
saudacao()