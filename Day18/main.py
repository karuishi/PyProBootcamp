from turtle import Turtle, Screen
from random import random, choice

fofo = Turtle()
fofo.shape("turtle")
fofo.color("red")

# Draw Square
# for move in range(4):
#     fofo.forward(100)
#     fofo.right(90)

# Draw dotted line
# for move in range(15):
#     fofo.forward(10)
#     fofo.penup()
#     fofo.forward(10)
#     fofo.pendown()

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon with a different color for each 
def change_pen_color():
    r = random()
    g = random()
    b = random()
    fofo.pencolor(r, g, b)

# def draw_shape(num_sides):    
#     angle = 360 / num_sides
#     for move in range(num_sides):
#         fofo.forward(100)
#         fofo.right(angle)

# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)
#     change_pen_color()

# Draw a random walk line with differente colors at each turn
# walk = True
# directions = [0, 90, 180, 270]
# fofo.pensize(15)
# fofo.speed("fastest")

# for _ in range(200):
#     change_pen_color()
#     fofo.forward(30)
#     fofo.setheading(choice(directions)) 

# Draw a spirograph
fofo.speed("fastest")

def draw_spirograph(size_gap):
    for _ in range(int(360 / size_gap)):
        change_pen_color()
        fofo.circle(100)
        fofo.setheading(fofo.heading() + size_gap)

draw_spirograph(5) 

screen = Screen()
screen.exitonclick()