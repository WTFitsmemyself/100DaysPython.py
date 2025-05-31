import random as r
import turtle as t


def random_color():
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    randomcolor = (red, green, blue)
    return randomcolor


obj_t = t.Turtle()
obj_t.pensize(3)
t.colormode(255)
obj_s = t.Screen()
obj_t.speed("fastest")
for _ in range(0, 45):
    obj_t.color(random_color())
    obj_t.circle(100)
    obj_t.right(10)

obj_s.exitonclick()

