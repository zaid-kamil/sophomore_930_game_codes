import pgzrun

WIDTH = 1000
HEIGHT = 600
bus = Actor('bus',pos=(50,50))
amb = Actor('ambulance',pos=(50,100))
car = Actor('sports_yellow',pos=(50,150))

def draw():
    screen.clear()
    bus.draw()
    amb.draw()
    car.draw()

def update():
    bus.x += 2
    if bus.x > WIDTH:
        bus.x = 0
        

pgzrun.go()