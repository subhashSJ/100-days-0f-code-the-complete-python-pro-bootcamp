from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def reset(self):
        for turtle in self.segments:
            turtle.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            (x, y) = self.segments[i-1].pos()
            self.segments[i].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not int(self.head.heading()) == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not int(self.head.heading()) == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not int(self.head.heading()) == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not int(self.head.heading()) == LEFT:
            self.head.setheading(RIGHT)
