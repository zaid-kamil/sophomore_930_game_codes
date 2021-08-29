import pgzrun

WIDTH = 500
HEIGHT = 500

player = Actor('tile_0040.png',pos=(100,HEIGHT-100))

def draw():
    screen.clear()
    player.draw()

def update():
    if keyboard.right:
        player.x += 2
    elif keyboard.left:
        player.x -= 2

    # up and down

pgzrun.go()