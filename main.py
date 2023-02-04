from pygame import *
from random import randint



bg = 'field.png'
ball = 'ball2.png'
st = 'stick.png'


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

back = (200, 255, 255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("PING_PONG")
background = transform.scale(image.load(bg), (win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60


gamer = Player(st,600, 200, 50, 100, -150)
gamer2 = Player2(st, 140, 200, 50, 100, 150)
ball = GameSprite('ball2.png', 200, 200, 46 ,50, 50)

font.init()
font1 = font.Font(None, 70)
lose1 = font1.render("PLAYER 1 LOSE", True, (180, 0, 0))
lose = font1.render("PLAYER 2 LOSE" , True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(back)
        gamer2.update()
        gamer.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(gamer, ball) or sprite.collide_rect(gamer2, ball):
            speed_x *= -1

        if ball.rect.y >= win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose, (200, 200))
            game_over = True 
                
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True 

        gamer.reset()
        gamer2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
