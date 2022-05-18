from turtle import Turtle, Screen

obj_t = Turtle()
obj_s = Screen()
obj_t.shape("turtle")
num_sides = [3, 4, 5, 6, 7, 8, 9, 10]
colors = ["green", "blue", "red", "#d7823a", "magenta", "Purple", "#b35a2a", "olive"]


def draw_shapes(num_sidess):
    angle = 360 / num_sidess
    for _ in range(num_sidess):
        obj_t.forward(100)
        obj_t.right(angle)


for i in range(0, len(num_sides)):
    obj_t.color(colors[i])
    sideX = num_sides[i]
    draw_shapes(sideX)


obj_s.exitonclick()
