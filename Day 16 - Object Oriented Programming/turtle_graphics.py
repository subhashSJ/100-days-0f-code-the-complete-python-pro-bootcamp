from turtle import Turtle, Screen

# Creating an object from a Turtle class
my_turtle = Turtle()
print(my_turtle)

my_turtle.shape("turtle")
my_turtle.color("red", "green")

# Drawing equilateral triangle with turtle
print(my_turtle.position())
my_turtle.forward(100)
my_turtle.left(120)
my_turtle.forward(100)
my_turtle.left(120)
my_turtle.forward(100)
print(my_turtle.position())


my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()