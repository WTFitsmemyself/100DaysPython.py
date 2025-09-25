import turtle
import pandas as pd


NUMBER_OF_STATES = 50
NUMBER_OF_USER_GUESSES = 0

IMG_PATH = "blank_states_img.gif"

data = pd.read_csv("./50_states.csv")
STATES_LIST = data['state'].to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape(IMG_PATH)
turtle.shape(IMG_PATH)

is_game_running = True

while is_game_running:
    ans_user = screen.textinput(title=f"Enter a State {NUMBER_OF_USER_GUESSES}/{NUMBER_OF_STATES}", prompt="What is another State?: ")
    if ans_user in STATES_LIST:
        print("You entered the " + ans_user)
        NUMBER_OF_USER_GUESSES += 1
        screen.update()
    else:
        is_game_running = False

screen.exitonclick()

