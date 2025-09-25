import turtle
import pandas as pd

NUMBER_OF_STATES = 50
NUMBER_OF_USER_GUESSES = 0

IMG_PATH = "blank_states_img.gif"

data = pd.read_csv("./50_states.csv")
STATES_LIST = data['state'].to_list()
user_guesses = []

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape(IMG_PATH)
turtle.shape(IMG_PATH)

pen = turtle.Turtle()
pen.hideturtle()

while NUMBER_OF_STATES != NUMBER_OF_USER_GUESSES:
    ans_user_state = screen.textinput(title=f"Enter a State {NUMBER_OF_USER_GUESSES}/{NUMBER_OF_STATES}", prompt="What is another State?: ").title()
    ans_user_x = int(data[data['state'] == ans_user_state].x)
    ans_user_y = int(data[data['state'] == ans_user_state].y)

    if ans_user_state in STATES_LIST:
        pen.penup()
        pen.goto(ans_user_x, ans_user_y)
        pen.write(f"{ans_user_state}", align="center", font=("Arial", 8, "normal"))
        NUMBER_OF_USER_GUESSES += 1
        user_guesses.append(ans_user_state)
        screen.update()

screen.mainloop()