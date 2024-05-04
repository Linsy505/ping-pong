from pygame import *

win_widht = 700
win_height = 500
display.set_caption("PING-PONG")
window = display.set_mode((win_widht, win_height))

back = (200, 255, 255)
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.sizeX = size_x
        self.sizeY = size_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < (win_widht - 5 - self.sizeX):
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < (win_widht - 5 - self.sizeX):
            self.rect.y += self.speed

racket1 = Player('racket.png', 30, 200, 60, 70, 4)
racket2 = Player('racket.png', 620, 200, 60, 70, 4)
ball = GameSprite('ball.jpg', 200, 200, 80, 50, 4)

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)
        display.update()
        racket1.update_l()
        racket2.update_r()

        racket1.reset()
        racket2.reset()
        ball.reset()

        display.update()
    time.delay(50)
