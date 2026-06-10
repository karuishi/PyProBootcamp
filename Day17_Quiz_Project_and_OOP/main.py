"""Criando uma nova classe e inicializando seu construtor"""
# Classe
class User: 
    # Construtor da classe
    def __init__(self, user_id, username): # Parâmetros do construtor (situacional)
        # Atributos dos objetos da classe
        self.id = user_id 
        self.username = username
        self.followers = 0
        self.following = 0

    # Criando um Método da classe
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Karuishi")
user_2 = User("002", "Hoott")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.followers)
print(user_2.followers)
print(user_2.followers)
