import pgzrun
import random

WIDTH = 800
HEIGHT = 300
# HEIGHT//2 makes the player in the middle of the screen vertically
# WIDTH//2 makes the player in the middle of the screen horizontally
p1 = Actor('tile_0040.png',pos=(20,HEIGHT//2))
item = Actor('tile_0052.png',pos=(100,100))

score = 0

def draw():
    screen.clear()
    # draw score, on top 5,5 pos and color white
    screen.draw.text(f'P1 score: {score}', (5,5), color='white')
    p1.draw()
    item.draw()

def update():
    global score
    move_player()
    # if player touch the item, add score
    if p1.colliderect(item):
        score += 1
        item.x = random.randint(0, WIDTH)
        item.y = random.randint(0, HEIGHT)
        

# function handle movement of player
def move_player():
    if keyboard.right and p1.x < WIDTH-10:
        p1.x += 2
    elif keyboard.left and p1.x > 10:
        p1.x -= 2
    elif keyboard.up and p1.y > 10:
        p1.y -= 2
    elif keyboard.down and p1.y < HEIGHT-10:
        p1.y += 2
    

pgzrun.go()

