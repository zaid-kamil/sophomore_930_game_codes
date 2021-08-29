import pgzrun
import random
import pygame

HEIGHT = 300
WIDTH = 520

def draw():
    screen.clear()
    for x in range(0, WIDTH, 40):
        y = random.randint(0, HEIGHT)
        screen.draw.filled_circle((x,y),20,'white')

    for x in range(0, WIDTH, 40):
        y = random.randint(0, HEIGHT)
        screen.draw.filled_circle((x,y),20,'white')

# example to go fullscreen when f is pressed
def update():
    if keyboard.f:
        pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)
    if keyboard.escape:
        exit()
pgzrun.go()