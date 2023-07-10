import pygame
from pygame.locals import *
import random as rand
import math

run = True
pygame.init()
win = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
food_on = False

class Snake():
    def __init__(self):
        self.pice = pygame.Rect([400, 400, 50, 50])
        self.body = [self.pice.copy()]
        self.lenght = 1
        self.fod = None
    def draw(self):
        for s in self.body:
            pygame.draw.rect(win, (0, 255, 0), s)
    def move(self, dx, dy):
        snake_dir = (dx, dy)
        self.pice.move_ip(snake_dir)
        self.body.append(self.pice.copy())
        self.body = self.body[-self.lenght:]
    def food(self, codrs):
        self.fod = self.pice.copy()
        self.fod.center = codrs
        pygame.draw.rect(win, (225, 0, 0), self.fod)

dx = 0
dy = 0
x = 0
y = 0
r = (0,0)

snake = Snake()

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dx = -50
        dy = 0
    if keys[pygame.K_RIGHT]:
        dx = 50
        dy = 0
    if keys[pygame.K_UP]:
        dy = -50
        dx = 0
    if keys[pygame.K_DOWN]:
        dy = 50
        dx = 0

    snake.move(dx, dy)
    pygame.time.wait(100)

    win.fill((51, 102, 225))
    for i in range(0, 900, 50):
        pygame.draw.line(win, (255, 255, 255), (0, i), (900, i))
        pygame.draw.line(win, (255, 255, 255), (i, 0), (i, 900))
    snake.draw()
    if food_on == False:
        r = (rand.randrange(50/2, 900 - 50 / 2, 50), rand.randrange(50/2, 900 - 50 / 2, 50))
        food_on = True

    snake.food(r)
    if r[0] == snake.pice.centerx and r[1] == snake.pice.centery:
        food_on = False
        snake.lenght += 1
    self_eat = pygame.Rect.collidelist(snake.pice, snake.body[:-1]) != -1
    if snake.pice.left < 0 or snake.pice.right > 900 or snake.pice.top < 0 or snake.pice.bottom > 900 or self_eat:
        run = False
    
    clock.tick(60)
    pygame.display.flip()
    pygame.display.update()
