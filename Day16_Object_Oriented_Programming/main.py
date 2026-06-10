# from turtle import Turtle, Screen

# # Criando um objeto chamado "fofo" a partir da classe "Turtle"
# fofo = Turtle() 
# print(fofo)
# my_screen = Screen()

# # Acessando um método do objeto criado
# fofo.shape("turtle")
# fofo.color("magenta4")
# fofo.forward(100)
# my_screen.exitonclick()

# # Acessando um atributo do objeto criado
# print(my_screen.canvheight)

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)