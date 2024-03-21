from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 250)
        self.score = 1
        self.hideturtle()
        self.create_score()

    def create_score(self):
        self.write(f"Level: {self.score}", align="left",font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
