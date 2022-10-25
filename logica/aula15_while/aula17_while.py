# Índices
# 0123456789......................33

frase = 'O rato roeu a roupa do rei de roma'
tamanho_da_frase = len(frase)
cont = 0
nova_string = ''

inputUsuario = input('Qual letra deseja colocar em maiúsculo: ')

while cont < tamanho_da_frase:
    #print(frase[cont], cont)
    letra = frase[cont]
    if letra == inputUsuario:
        nova_string += inputUsuario.upper()
    else:
        nova_string += letra
    cont += 1
print(nova_string)