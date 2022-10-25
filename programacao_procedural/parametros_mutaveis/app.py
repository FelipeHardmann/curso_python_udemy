
def listaClientes(clientesIteravel, lista=[]): #Quando você coloca um parametro mutavel ele muda o paramêtro inteiro
    if lista is None:
        lista = [] #Dessa forma a lista não vai add os elementos antigos ou novos, se tornaram listas independentes
    lista.extend(clientesIteravel)
    return lista

listaClientes1 = ['Fabrício']
clientes1 = listaClientes(['João', 'Maria', 'Eduardo'], listaClientes1) #Dessa forma você pode corrigir o "erro"
clientes2 = listaClientes(['Marcos', 'Jonas', 'Zico'])

#Aqui ele só está alongando a mesma lista

print(clientes1)
print(clientes2)
