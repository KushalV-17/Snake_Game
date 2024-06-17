from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",18,"normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.pendown()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)


    def increseScore(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)