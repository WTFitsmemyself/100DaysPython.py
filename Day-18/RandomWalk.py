from random import choice, randint
from turtle import Turtle, Screen, colormode

Distance = 30
Rotate = [0, 90, 180, 270]
s_obj = Screen()
t_obj = Turtle()
t_obj.pensize(3)
colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    randomcolor = (r, g, b)
    return randomcolor


while True:
    t_obj.pencolor(random_color())
    t_obj.forward(Distance)
    t_obj.setheading(choice(Rotate))

s_obj.exitonclick()
