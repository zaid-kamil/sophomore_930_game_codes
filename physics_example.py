import pgzrun

WIDTH = 500
HEIGHT = 500

ball = Actor('ball',pos=(150,300))
bat = Rect((200,380),(60,20))
a = Rect((250,100),(80,20))

vx = 2
vy = 2

def draw():
    screen.clear()
    ball.draw()
    screen.draw.filled_rect(bat,'white')
    screen.draw.filled_rect(a,'green')

def update():
    global vx,vy
    ball.x += vx
    ball.y += vy
    if ball.right > WIDTH or ball.left < 0:
        vx = -vx # negative vx means move left 
    if ball.colliderect(bat) or ball.top < 0 :
        vy = -vy   
    if ball.colliderect(a):
        vx = -vx
        vy = -vy
    if ball.bottom >HEIGHT:
        exit()
    if keyboard.right:
        bat.x += 2
    elif keyboard.left:
        bat.x -= 2

pgzrun.go()
    
# 1. add score text to the game
# 2. add image of a ball instrad of red rectangle
# 3. add a logic to make the green box disappear when ball collides with it 2 times
# 4. add two more blocks(green box) on top side of screen for colliding with ball
# 5. update the score when the green box is removed from screen