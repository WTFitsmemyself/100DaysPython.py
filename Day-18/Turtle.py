from turtle import Turtle, Screen

Tim = Turtle()
Tim.shape("arrow")
Tim.color("#994184")
Tim.pensize(3)
screen = Screen()
for _ in range(15):
    Tim.forward(10)
    Tim.penup()
    Tim.forward(10)
    Tim.pendown()

screen.exitonclick()
