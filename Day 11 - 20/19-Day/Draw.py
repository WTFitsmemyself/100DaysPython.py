from turtle import Turtle, Screen


class Movements:
    def __init__(self, moveSize):
        self.tim = Turtle()
        self.movement_size = moveSize

    def move_forward(self):
        self.tim.forward(self.movement_size)

    def move_backward(self):
        self.tim.backward(self.movement_size)

    def move_counter_clockwise(self):
        self.tim.left(self.movement_size)

    def move_clockwise(self):
        self.tim.right(self.movement_size)


tim = Movements(10)
screen = Screen()
screen.onkey(fun=tim.move_forward, key="w")
screen.onkey(fun=tim.move_backward, key="s")
screen.onkey(fun=tim.move_counter_clockwise, key="a")
screen.onkey(fun=tim.move_clockwise, key="d")
screen.listen()
screen.exitonclick()
