from random import choice
from turtle import Turtle, Screen
import csv

hex_file = open("./hex_code.csv", 'w')

writer = csv.writer(hex_file)

movement_step = 10
max_movement_line = 1000
dot_size = 5

colors = ["#8a3ec9",
          "#c7a6cd",
          "#fefddc",
          "#197168",
          "#2ebe03",
          "#fed401",
          "#e37929",
          "#648ade",
          "#9cd0dd",
          "#f6f595",
          "#b43856"]


def random_color():
    color_selected = choice(colors)
    writer.writerow(str(color_selected).split(","))
    return color_selected


obj_s = Screen()
obj_s.bgcolor("#2f1b35")
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
            obj_t.forward(movement_step)
            obj_t.pendown()
        obj_t.setheading(90)
        obj_t.penup()
        obj_t.forward(movement_step)
        obj_t.setheading(180)
        obj_t.forward(max_movement_line)
        obj_t.setheading(0)
        obj_t.pendown()


init_move()
movement()
obj_t.ht()
hex_file.close()
obj_s.exitonclick()
