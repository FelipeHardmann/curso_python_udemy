#Aqui são todas as formas que eu posso importar pacotes no Python
import vendas.calcPreco
from vendas import calcPreco
from vendas.calcPreco import aumento, reducao
from vendas.formata import preco

valor = 49.90
preco_atual = aumento(valor, 15)
print(preco_atual)

preco_reduzido = reducao(valor, 15)
print(preco_reduzido)


