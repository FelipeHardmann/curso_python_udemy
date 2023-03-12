'''
Utilizando o método call para colocarmos o nosso objeto como executável
'''

class CallMe:
    def __init__(self, phone: str) -> None:
        self.phone = phone

    def __call__(self, nome: str) -> None:
        print(f'{nome} está chamando {self.phone}')


call = CallMe('719829883')
call('Felipe')
