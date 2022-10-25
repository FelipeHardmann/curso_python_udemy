from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A' },
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'José', 'nota': 'B'}
]

ordena = lambda item: item['nota']
alunos.sort(key = ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valoresAgrupado in alunos_agrupados:
    print(f'Agrupamento {agrupamento}')
    print(f'{len(list(valoresAgrupado))} tiraram a nota {agrupamento}')
    '''
    for aluno in valoresAgrupados:
        print(aluno)
    '''