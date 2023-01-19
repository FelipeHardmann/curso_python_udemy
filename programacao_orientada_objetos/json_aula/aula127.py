# Exercício salve sua classe em JSON
# Salve os dados da sua classe em JSON 
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados

import json

caminho_arquivo = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Felipe', 22)
p2 = Pessoa('Artur', 25)
p3 = Pessoa('Mateus', 32)
bd = [vars(p1), vars(p2), vars(p3)]

with open(caminho_arquivo, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
