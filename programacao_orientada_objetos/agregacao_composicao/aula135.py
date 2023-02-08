# A agregação signifca dizer que um pode existir sem o outro porém, eles são primordias 
# para um funcionamento bom
# Um bom exemplo disso é o carro e a roda, onde o carro pode existir sem a roda e vice versa
#  Porém, não funcionam bem separados

class Carrinho:
    def __init__(self) -> None:
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def listar(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

    def inserir(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

    
class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir(p1, p2)
carrinho.listar()
