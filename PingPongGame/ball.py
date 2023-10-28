from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.up()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05
    # def move(self, flag):
    #     if flag == 0:
    #         new_x = self.xcor() + 5
    #         new_y = self.ycor() + 5
    #         self.goto(new_x, new_y)
    #     elif flag == 1:
    #         new_x = self.xcor() + 5
    #         new_y = self.ycor() - 5
    #         self.goto(new_x, new_y)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_hit(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.move_speed = 0.05
        self.goto(0, 0)
        self.x_move *= -1

