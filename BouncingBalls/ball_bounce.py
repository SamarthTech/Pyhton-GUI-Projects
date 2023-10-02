import pygame,time,random
pygame.init()

screen=pygame.display.set_mode((800,600))
background=pygame.image.load('background-img.jpg')
pygame.display.set_caption('Ball Bounce Simulation')

class ball:
    ball_image=pygame.image.load('ball.png')
    g=1
    def __init__(self):
        self.velocityX=4
        self.velocityY=4
        self.X=random.randint(0,768)
        self.Y=random.randint(0,350)

    def render_ball(self):
        screen.blit(ball.ball_image, (self.X,self.Y))
    def move_ball(self):
        self.velocityY+=ball.g
        self.X+=self.velocityX
        self.Y+=self.velocityY
        if self.X<0 or self.X>768:
            self.velocityX*=-1
        if self.Y<0 and self.velocityY<0:
            self.velocityY*=-1
            self.Y=0
        if self.Y>568 and self.velocityY>0:
            self.velocityY*=-1
            self.Y=568
Ball_List=[ball(),ball(), ball(), ball(), ball()]
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    time.sleep(0.02)
    screen.blit(background, (0,0))
    for ball_item in Ball_List:
        ball_item.render_ball()
        ball_item.move_ball()
    pygame.display.update()