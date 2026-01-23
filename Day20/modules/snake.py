from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake() # Ao ser instanciado por um objeto, automaticamente já engatilha este método
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)        
    
    # Add a new segment to the snake
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        """
        Start = len(sengments) -1 (índice do último segmento) 
        Stop = 0 (o loop para no índice 1)
        Step = -1 (Conta de trás para frente)
        
        Se a cobra tem 3 segmentos (índices 0, 1, 2), 
        o loop vai rodar para seg_num = 2 e depois para seg_num = 1.
        O loop executa as seguintes trocas:

        Iteração 1 (seg_num = 2):
            Pega a posição do segmento da frente (seg_num - 1, ou seja, índice 1).
            Move o segmento 2 (Cauda) para a posição do segmento 1 (Meio).
            Resultado: A cauda vai para (-20, 0).

        Iteração 2 (seg_num = 1):
            Pega a posição do segmento da frente (seg_num - 1, ou seja, índice 0).
            Move o segmento 1 (Meio) para a posição do segmento 0 (Cabeça).
            Resultado: O meio vai para (0, 0).
        """
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    """Controla os movimentos da cabeça da cobra e a impede de mover backwards """
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
