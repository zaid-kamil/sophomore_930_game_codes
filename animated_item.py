import pgzrun


HEIGHT = 500
WIDTH = 500

p1 = Actor('tile_0040.png',pos=(20,20))
bee = Actor('tile_0051.png',pos=(20,50))

p1_images = ['tile_0040.png','tile_0041.png']
p1_img_num = 0

b1_images = ['tile_0051.png','tile_0052.png']
b1_img_num = 0

def draw():
    screen.clear()
    p1.draw()
    bee.draw()

def update():
    if keyboard.left:
        p1.x -= 2
    if keyboard.right:
        p1.x += 2

def animate_p1():
    global p1_img_num
    p1.image = p1_images[p1_img_num % len(p1_images)] # 0 % 2 = 0, 1 % 2 = 1
    p1_img_num += 1

def animate_bee():
    global b1_img_num
    bee.image = b1_images[b1_img_num % len(b1_images)]
    b1_img_num += 1

clock.schedule_interval(animate_p1, .2)
clock.schedule_interval(animate_bee, .2)

pgzrun.go()