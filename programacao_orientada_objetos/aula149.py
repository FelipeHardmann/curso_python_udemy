# with open('aula149.txt', 'w') as arquivo:
#     ...

class MyContextManager:
    def __init__(self, caminho, modo):
        self.caminho = caminho
        self.modo = modo
        self.arquivo = None
    
    def __enter__(self):
        print('Abrindo arquivo')
        self.arquivo = open(self.caminho, self.modo)
        return self.arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando arquivo')
        self.arquivo.close()


with MyContextManager('aula149.txt', 'w') as arquivo:
    arquivo.write('Linhas 1 ')
    arquivo.write('Linhas 2 ')
    arquivo.write('Linhas 3 ')
    print('WITH', arquivo)
