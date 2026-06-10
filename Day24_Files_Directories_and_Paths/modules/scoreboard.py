from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_high_score()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()
        
    def read_high_score(self):
        with open("data.txt") as data:
            self.high_score = int(data.read())
    
    def write_high_score(self):
        with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")