from pessoa import Pessoa

p1 = Pessoa('Felipe', 22)
p2 = Pessoa('Luiz', 29)

'''p1.comer('maçã')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('Alimento')
p1.parar_comer()
p1.falar('assunto')'''

p1.falar('POO')
p2.falar('Filmes')
p1.comer('Churrasco')

print(p1.ano_atual)
print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

# Tentando modificar algo
