import pgzrun
import os

WIDTH = 610
HIGHT = 417
os.environ["SDL_VIDEO_CENTERED"] = '1'

backGround = Actor("back")
car1 = Actor("car1",(355,320))
car2 = Actor("car2",(345,350))

car1Nfs = True
car2Nfs = True


def draw():
    backGround.draw()
    car1.draw()
    car2.draw()

def update():
    global car1Nfs , car2Nfs
    if keyboard.up :
        car1.y -= 2
    if keyboard.down :
        car1.y += 2
    if keyboard.left :
        car1.x -= 2
    if keyboard.right :
        car1.x += 2
    if keyboard.p and car1Nfs != False :
        car1.y -= 50
        car1Nfs = False
    

    if keyboard.w :
        car2.y -= 2
    if keyboard.s :
        car2.y += 2
    if keyboard.a :
        car2.x -= 2
    if keyboard.d :
        car2.x += 2
    if keyboard.z and car2Nfs != False :
        car2.y -= 50
        car2Nfs = False
    
pgzrun.go()
