class A:
    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, '_jaexiste'):
            cls._jaxiste = object.__new__(cls)

        return cls._jaxiste
    
    def __init__(self):
        print('INIT')


a = A()
b = A()
c = A()

print(id(a), id(b), id(c))