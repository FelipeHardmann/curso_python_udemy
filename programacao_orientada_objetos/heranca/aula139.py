# super() é uma super classe na sub classe
# Classe Principal (Pessoa)
#   -> super class, base class, parent class
# Classes filas (Cliente)
#   -> sub class, child class, derived class

class MinhaString(str):
    def upper(self):
        print('Chamou o upper')
        returno = super().upper()
        return returno

    
string = MinhaString('Felipe')
print(string.upper())
