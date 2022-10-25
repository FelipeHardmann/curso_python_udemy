from vendas.formata import preco

def aumento(valor, porcentagem, formata=False):
    r = valor + (valor * (porcentagem / 100))
    if format:
        return preco.real(r)
    else:
        return r

def reducao(valor, porcentagem, formata=False):
    r = valor - (valor * (porcentagem / 100))
    if format:
        return preco.real(r)
    else:
        return r