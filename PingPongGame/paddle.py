from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.up()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
