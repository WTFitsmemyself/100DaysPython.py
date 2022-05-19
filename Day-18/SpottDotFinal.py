from random import choice
from turtle import Turtle, Screen

movement = 10
max_movement_line = 1000
dot_size = 5

colors = ["medium spring green",
          "dark cyan",
          "floral white",
          "light pink",
          "medium violet red",
          "thistle",
          "peach puff",
          "orange",
          "moccasin",
          "olive",
          "green yellow",
          "dark orchid"]


def random_color():
    return choice(colors)


obj_s = Screen()
obj_t = Turtle()
obj_t.speed("fastest")


def init_move():
    obj_t.setheading(225)
    obj_t.penup()
    obj_t.forward(700)
    obj_t.setheading(0)
    obj_t.pendown()


def movement():
    for i in range(0, 100):
        for j in range(0, 100):
            obj_t.dot(dot_size, random_color())
            obj_t.penup()
            obj_t.forward(movement)
            obj_t.pendown()
        obj_t.setheading(90)
        obj_t.penup()
        obj_t.forward(movement)
        obj_t.setheading(180)
        obj_t.forward(max_movement_line)
        obj_t.setheading(0)
        obj_t.pendown()


init_move()
movement()

obj_s.exitonclick()
