import json
from aula127 import caminho_arquivo, Pessoa

with open(caminho_arquivo, 'r') as arquivo:
    dados = json.load(arquivo)
    p1 = Pessoa(**dados[0])

    print(p1.nome)
