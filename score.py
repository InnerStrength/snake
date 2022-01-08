from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, 'normal')

class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.refresh_board()

    def refresh_board(self):
        self.clear()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.setpos(0, 270)
        self.write(f"Points : {self.score}     High score: {self.high_score}",
                   True, align=ALIGNMENT, font=FONT)


    def add(self):
        self.score += 1
        self.refresh_board()

    def new_game(self):
        self.score = 0
        self.refresh_board()

    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))

