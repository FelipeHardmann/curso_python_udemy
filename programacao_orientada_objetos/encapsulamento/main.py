# Encapsulamento
# Serve para esconder certas partes do código
# Protegendo algumas partes do código

'''
public(São métodos que podem ser acessados dentro e fora da classe),
protected _ (São métodos que podem ser acessados apenas dentro ou das filhas da classe) 
private __ (Só fica disponível dentro da classe)
'''
# Ajeitando gitgg

#O protected é um privado mais fraco(Praticamente Público) que não precisa de tratamento, apenas se recomenda
# não utilizar essa variável 

# Apenas o privado precisa de tratamento
# Quando é privado você fala ao desenvolvedor que não é para acessar a classe 
# de maneira NENHUMA

class BaseDeDados:
    def __init__(self): #Construtor
        self.__dados = {} 

    @property
    def dados(self): #Dessa forma você faz com que um método da classe se torne um atributo
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome, sep=' - ')

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Felipe')
bd.inserir_cliente(2, 'Luiz')
print(bd.dados)
# print(bd.__dados) mesmo com o método protegido você consegue acessar
# bd.dados = 'Um outra coisa' #Se fizer isso com um método público, você quebra todo o código
