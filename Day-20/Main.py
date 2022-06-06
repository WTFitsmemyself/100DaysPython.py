from turtle import Turtle, Screen
snakes_part = []
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
x_positions = [0, -20, -40]
y_position = 0
for i in range(3):
    snake = Turtle()
    snake.shape("square")
    snake.color("white")
    snake.penup()
    snake.goto(x=x_positions[i], y=y_position)
    snakes_part.append(snake)

print(snakes_part)
screen.exitonclick()
