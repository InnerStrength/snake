from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.reset_pos()

    def reset_pos(self):
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.setpos(randint(-13, 13)*20, randint(-13, 13)*20)

