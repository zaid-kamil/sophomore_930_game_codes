import pgzrun
import pygame

WIDTH = 600
HEIGHT = 600

player = Actor("tile_0040",pos=(50,50))
en1 = Actor('tile_0052',pos=(50,300))

# make the player surface transform in scale to 50,50
player._surf = pygame.transform.scale(player._surf,(50,50))
player._update_pos()

en1._surf = pygame.transform.scale(en1._surf,(50,50))
en1._update_pos()

move_forward = True

def draw():
    screen.clear()
    player.draw()
    en1.draw()

def update():
    global move_forward # permit this function to change vale of move_forward

    if move_forward == True: # check if move_forward is true
        player.y += 3
        if player.y > HEIGHT:
            player.y = 0
    else:
        player.y -= 3
        if player.y < 0:
            player.y = HEIGHT

    if player.colliderect(en1):
        move_forward = not move_forward
   

pgzrun.go()