import pgzrun

WIDTH = 600
HEIGHT = 280
SIGN_POS_Y = HEIGHT - 67 # common pos of street signs
bus = Actor('bus',pos=(50,HEIGHT-50))
car = Actor('sports_yellow',pos=(250,HEIGHT-50))
amb = Actor('ambulance_r',pos=(50,HEIGHT-65))
background = Actor('game_bg') # not position means that it starts from 0,0
light_1 = Actor('light',pos=(100,SIGN_POS_Y))
light_2 = Actor('light',pos=(300,SIGN_POS_Y))
sign_b = Actor('sign_blue',pos=(200,SIGN_POS_Y))
sign_s = Actor('sign_street',pos=(WIDTH-100,SIGN_POS_Y))

def  draw():
    screen.clear()
    background.draw()
    light_1.draw()
    light_2.draw()
    sign_b.draw()
    sign_s.draw()
    amb.draw()
    car.draw()
    bus.draw()
    

def update():
    # left to right
    bus.x += 2
    if bus.x > WIDTH:
        bus.x = 0
    # left to right
    car.x += 3
    if car.x > WIDTH:
        car.x = 0
    # right to left
    amb.x -=2   
    if amb.x < 0:
        amb.x = WIDTH 
        
pgzrun.go()
