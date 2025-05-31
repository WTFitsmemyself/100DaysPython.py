import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.generate_food_location()

    def generate_food_location(self):
        x_value_food = random.randint(-280, 280)
        y_value_food = random.randint(-280, 280)
        food_location = (x_value_food, y_value_food)
        self.goto(food_location)
