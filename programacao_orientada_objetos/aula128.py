# method vs @classmethod vs @staticmethod
# method - self, método de instância 
# @classmethod - cls, método de classe
# @staticmethod - método etático (Xself, Xcls)

class Connection:
    def __init__(self, host='host'):
        self.host = host
        self.user = None
        self.passwd = None

    def set_user(self, user):
        # setter
        self.user = user

    def set_passwd(self, password):
        self.passwd = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.passwd = password
        return connection

    # Um método que não recebe nada nem classe nem o self 
    @staticmethod
    def soma(x, y):
        return x + y


# c1 = Connection()
c1 = Connection.create_with_auth('Luiz', '1234')
# c1.set_user('Luiz')
# c1.set_passwd('1234')
print(c1.user)
print(c1.passwd)
