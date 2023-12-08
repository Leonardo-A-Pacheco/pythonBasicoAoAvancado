# method vs classmethod vs staticmethod
# method - self metodo de instancia
# method classmethod cls metodo de clsse 
# staticmethod metodo estatico {nao tem acesso nem ao cls nem ao self}
# 211
class Conection:
    def __init__(self, host= 'localhost'):
        self.host = host
        self.user = None
        self.password = None
    
        #setter
    def set_user(self, user):
        self.user = user
  
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def soma(x, y):
        return x + y


# c1 = Conection()
c1 = Conection.create_with_auth('leonardo', '1234qwer')
print(c1.user)

c1.set_user('Leonardo')
c1.set_password('blablabla11347')

print(c1.user)
print(c1.password)


print(f'\n função de classe estatica{Conection.soma(2,5)}')






