from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(height=500, width=500)
screen.bgcolor("black")
colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]
x_position = -230
y_positions = [70, 40, 10, -20, -50, -80]
all_turtles = []
match_is_on = False


def turtle_settle():
    for turtles_in in range(0, 6):
        tim = Turtle()
        tim.shape("turtle")
        tim.penup()
        tim.color(colors[turtles_in])
        tim.goto(x=x_position, y=y_positions[turtles_in])
        all_turtles.append(tim)


user_bet = screen.textinput("Who will win?", "Please insert the color you think will win:")

if user_bet:
    match_is_on = True
turtle_settle()


while match_is_on:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            match_is_on = False
            winner = turtles.pencolor()
            if winner == user_bet:
                print("You Win")
            else:
                print(f"Your Loose color {winner} is winner")

        rand_distance = randint(0, 10)
        turtles.forward(rand_distance)

screen.exitonclick()
