from turtle import Turtle, Screen
from modules.snake import Snake
from modules.food import Food
from modules.scoreboard import ScoreBoard
import time

WALL = 290

screen = Screen()
screen.setup(width=600, height=600) # x axis = 300, -300 | y axis = 300, -300
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # Utilizado com o valor "zero" cancela a animação porém deixa a tela sem info

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update() # Traz de volta a info da tela, utilizado usualmente em conjunto com o tracer
    time.sleep(0.1) 
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        
    # Detect collision with wall
    if snake.head.xcor() > WALL or snake.head.xcor() < -WALL or snake.head.ycor() > WALL or snake.head.ycor() < -WALL: 
        # 280 = xy axis(300) - turtle size(20)
        score.reset()
        snake.reset()
        
    # Detect collision with tail
    for segment in snake.segments[1:]: # slicing, incluindo somente a head
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()