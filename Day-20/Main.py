from turtle import Screen
from snake import Snake
from time import sleep
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")


game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.snake_moves()
    print(snake.cord_of_snake())
    snake.snake_lose_or_not()

    if snake.head.distance(food) < 15:
        food.generate_food_location()

screen.exitonclick()
