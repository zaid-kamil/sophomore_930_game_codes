import pgzrun

WIDTH = 1000
HEIGHT = 600

def draw():
    screen.fill("white")
    screen.draw.circle((WIDTH//2, HEIGHT//2),250,"red")
    screen.draw.filled_circle((200,200),100,"green")
    screen.draw.line((100,50),(300, 50), "blue") # horizontal line
    screen.draw.line((100,50),(300, 200), "blue") # diagonal line
    screen.draw.line((100,50),(100, 300), "blue") # vertical line

pgzrun.go()