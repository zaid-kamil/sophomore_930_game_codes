# this will create a window with a rectangle and a circle
import pgzrun

WIDTH = 500 # width of window
HEIGHT = 500 # height of window

box = Rect((0,0),(50,50))
box2 = Rect((100,50),(75,100))
box3 = Rect((400,400),(50,50))
# the function the draws items on the game window for only first time
def draw():
    screen.clear() # clears the screen
    screen.draw.filled_rect(box,"green")
    screen.draw.filled_rect(box2,"red")
    screen.draw.filled_rect(box3,"blue")

# the function the handles item on the game window for every second after draw() 
def update():
    
    box.x += 1
    # bring the box to the left side of the screen
    if box.x > WIDTH:
        box.x = 0

    box2.y += 1
    if box2.y > HEIGHT:
        box2.y = 0

    box3.x += 2
    box3.y += 3
    if box3.x > WIDTH:
        box3.x = 0
    if box3.y > HEIGHT:
        box3.y = 0

    # move the box4 and box5 in reverse
    
# run the game
pgzrun.go()
