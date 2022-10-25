perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '6'
        },
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6'
        },
        'resposta_certa': 'c'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 9/3? ',
        'respostas': {
            'a': '3',
            'b': '4',
            'c': '1'
        },
        'resposta_certa': 'a'
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 10*10? ',
        'respostas': {
            'a': '80',
            'b': '100',
            'c': '6'
        },
        'resposta_certa': 'b'
    }
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua rsposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Você acertou!!!')
        respostas_certas += 1
    else:
        print('Você errou =/')

    print()

quantidade_perguntas = len(perguntas)
porcetagem = respostas_certas / quantidade_perguntas * 100

print(f'Você acertou {respostas_certas} perguntas.')
print(f'Sua porcentagem de acerto foi de {porcetagem}%')
