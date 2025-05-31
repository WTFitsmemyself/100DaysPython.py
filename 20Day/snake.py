from turtle import Turtle
MOVEMENT_SPEED = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.MAXIMUM_MOVE = (300, -300)
        self.snakes_part = []
        self.x_positions = [0, -20, -40]
        self.y_position = 0
        self.create_snake()
        self.head = self.snakes_part[0]

    def create_snake(self):
        for position in self.x_positions:
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.goto(x=position, y=self.y_position)
            self.snakes_part.append(snake)

    def snake_moves(self):
        for seg in range(len(self.x_positions) - 1, 0, -1):
            x_value = self.snakes_part[seg - 1].xcor()
            y_value = self.snakes_part[seg - 1].ycor()
            self.snakes_part[seg].goto(x=x_value, y=y_value)
        self.head.forward(MOVEMENT_SPEED)

    def cord_of_snake(self):
        while True:
            x_value = self.head.xcor()
            y_value = self.head.ycor()
            return x_value, y_value

    def snake_lose_or_not(self):
        x_value, y_value = self.cord_of_snake()
        if x_value == self.MAXIMUM_MOVE[1]:
            print("You loose")
            exit(1)
        elif x_value == self.MAXIMUM_MOVE[0]:
            print("You loose")
            exit(1)
        elif y_value == self.MAXIMUM_MOVE[0]:
            print("You loose")
            exit(1)
        elif y_value == self.MAXIMUM_MOVE[1]:
            print("You loose")
            exit(1)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
