# Modificadores de acesso

class Foo:
    def __init__(self) -> None:
        self.public = 'Publico'
        self._protected = 'Protegido'
        self.__private = 'Private'

    @property
    def private(self):
        return self.__private

    @private.setter
    def private(self, valor_private):
        self.__private = valor_private


f = Foo()
print(f.private)
