# example of a program that uses a boundary to check for keyboard input and move player

import pgzrun

WIDTH = 500
HEIGHT = 300

player = Actor('tile_0040.png',pos=(20,20))

def draw():
    screen.clear()
    player.draw()

def update():
    move_player()

# function handle movement of player
def move_player():
    if keyboard.right and player.x < WIDTH-10:
        player.x += 2
    elif keyboard.left and player.x > 10:
        player.x -= 2
    elif keyboard.up and player.y > 10:
        player.y -= 2
    elif keyboard.down and player.y < HEIGHT-10:
        player.y += 2

pgzrun.go()