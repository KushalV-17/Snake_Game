from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_X =random.randint(-275,275)
        random_Y =random.randint(-275,275)
        self.goto(random_X,random_Y)


    def refresh(self):
        random_X =random.randint(-275,275)
        random_Y =random.randint(-275,275)
        self.goto(random_X,random_Y)

