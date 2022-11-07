'''
Animal -> respirar
    Lobo(Animal) -> respirar / uivar
    Cachorro -> respirar / uivar / latir
'''

'''
Biblioteca -> chama_interface 
    Interface(Biblioteca) -> metodo_interface
        metodo_da_interface
'''


from classes.interface import Interface

i1 = Interface()
i1.chama_metodo_interface()