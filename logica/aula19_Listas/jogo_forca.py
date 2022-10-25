secreto = 'secreto'
errados = []
chance = 3


while True:
    if chance <= 0:
        print('Você perdeu!!')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Ah isso não vale, digite apenas uma letra')
        continue
    errados.append(letra)
    if letra in secreto:
        print(f'Acertou!! a letra {letra} existe na palavra secreta')
    else:
        print(f'A letra {letra} não existe na palavra secreta')
        errados.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in errados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f'Parabéns você ganhou!!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chance -= 1

    print(f'Você ainda {chance} chances.')
    print()