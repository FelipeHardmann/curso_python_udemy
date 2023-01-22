# method vs @classmethod vs @staticmethod 
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (xSelf, xCls)


class Connection:
    def __init__(self, host='localhost') -> None:
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self, password):
        self.password = password

# Esse método retorna a mesma coisa que os dois de cima
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection


c1 = Connection()
c1.set_user('Felipe')
print(c1.user)
