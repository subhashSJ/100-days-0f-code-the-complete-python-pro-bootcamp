from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")

# Drawing the square
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

timmy_the_turtle.penup()
timmy_the_turtle.goto(-150, -150)

# Drawing the dashed line
for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()



screen = Screen()
screen.exitonclick()