import pygame as game
import random
import time
game.init()
game.mixer.init()
game.mixer.music.load("sf\\dino3.mp3")
game.mixer.music.play()
def draws(dis,x,y):
    game.draw.line(dis,WHITE,[4+x,17+y],[4+x,7+y], 2)
    game.draw.line(dis,WHITE,[4+x,17+y],[9+x,27+y], 2)
    game.draw.line(dis,WHITE,[4+x,17+y],[-1+x,27+y], 2)
    game.draw.line(dis,WHITE,[4+x,7+y],[8+x,17+y], 2)
    game.draw.line(dis,WHITE,[4+x,7+y],[0+x,17+y], 2)
    game.draw.ellipse(dis,WHITE,[0+x,0+y,10,10],0)
    game.draw.ellipse(dis,BLACK,[0+x,0+y,10,10],2)
font_style = game.font.SysFont("comicsansms", 30)
BLACK = (0, 0, 0)
pink=(255,0,255)
WHITE = (255, 255, 255)
ash = (100,100,100)
dark_blue=(167, 16, 25)
blue = (30, 13, 23)
size = (1280,720)
yellow = (255, 255, 102)
ysc=(5,205,5)
dis = game.display.set_mode(size)
game.display.set_caption("stickman")
state= False
clock = game.time.Clock()
game.mouse.set_visible(0)
ht=game.image.load("pf\\ht.png" )
ht=game.transform.scale(ht,(90,70))
def message1(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [50, 30])
def message3(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [900,30])
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [250, 250])
def message2(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [440,310])
def message4(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [500,370])
xc =0
yc = 720
xs = 0
ys = 0
yo1=660
yo2=yo1-60
yo3=yo2-60
yo4=yo3-60
yo5=yo4-60
yo6=yo5-60
yo7=yo6-60
yo8=yo7-60
yo9=yo8-60
yo10=yo9-60
yo11=yo10-60
a1=random.randrange(20,1250,10)
b1=a1+random.randrange(20,40)
a2=random.randrange(20,1250,10)
b2=a2+random.randrange(20,40)
a3=random.randrange(20,1250,10)
b3=a3+random.randrange(20,40)
a4=random.randrange(20,1250,10)
b4=a4+random.randrange(20,40)
a5=random.randrange(20,1250,10)
b5=a5+random.randrange(20,40)
a6=random.randrange(20,1250,10)
b6=a6+random.randrange(20,40)
a7=random.randrange(20,1250,10)
b7=a7+random.randrange(20,40)
a8=random.randrange(20,1250,10)
b8=a8+random.randrange(20,40)
a9=random.randrange(20,1250,10)
b9=a9+random.randrange(20,40)
a10=random.randrange(20,1250,10)
b10=a10+random.randrange(20,40)
a11=random.randrange(20,1250,10)
b11=a11+random.randrange(20,40)
while not state:
    for event in game.event.get():
        if event.type==game.QUIT:
            state=True
        if event.type==game.KEYDOWN:
            if event.key==game.K_LEFT:
                xs=-3
            if event.key==game.K_RIGHT:
                xs=3
            if event.key == game.K_UP:
                ys=-3
        if event.type==game.KEYUP:
            if event.key==game.K_LEFT:
                xs=0
            if event.key==game.K_RIGHT:
                xs=0
            if event.key==game.K_UP:
                ys=3
    if xc>=1260:
        xs=0
        xc-=1
    elif xc<=13:
        xp=0
        xc+=1
    elif yc>680:
        ys=0
        yc-=1
    elif yc<=13:
        ys=0
        yc+=1
    else:
        xc+=xs
        yc+=ys
    if xc in range(0,50) and yc in range (570,590):
        ys=0
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\commingdown.mp3"))
        yc-=1
    if yc in range(yo1-30,yo1-10) and xc not in range(a1,b1):
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\going up.mp3"))
        ys=3
    if xc in range(a1,b1) and yc in range (yo1-30,yo1-10):
        ys=0
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\commingdown.mp3"))
        yc-=1
    if yc in range(yo2-30,yo2-10) and xc not in range(a2,b2):
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\going up.mp3"))
        ys=3
    if xc in range(a2,b2) and yc in range (yo2-30,yo2-10):
        ys=0
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\commingdown.mp3"))
        yc-=1
    if yc in range(yo3-30,yo3-10) and xc not in range(a3,b3):
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\going up.mp3"))
        ys=3
    if xc in range(a3,b3) and yc in range (yo3-30,yo3-10):
        ys=0
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\commingdown.mp3"))
        yc-=1
    if yc in range(yo4-30,yo4-10) and xc not in range(a4,b4):
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\going up.mp3"))
        ys=3
    if xc in range(a4,b4) and yc in range (yo4-30,yo4-10):
        ys=0
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\commingdown.mp3"))
        yc-=1
    if yc in range(yo5-30,yo5-10) and xc not in range(a5,b5):
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\going up.mp3"))
        ys=3
    if xc in range(a5,b5) and yc in range (yo5-30,yo5-10):
        ys=0
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\commingdown.mp3"))
        yc-=1
    if yc in range(yo6-30,yo6-10) and xc not in range(a6,b6):
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\going up.mp3"))
        ys=3
    if xc in range(a6,b6) and yc in range (yo6-30,yo6-10):
        ys=0
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\commingdown.mp3"))
        yc-=1
    if yc in range(yo7-30,yo7-10) and xc not in range(a7,b7):
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\going up.mp3"))
        ys=3
    if xc in range(a7,b7) and yc in range (yo7-30,yo7-10):
        ys=0
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\commingdown.mp3"))
        yc-=1
    if yc in range(yo8-30,yo8-10) and xc not in range(a8,b8):
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\going up.mp3"))
        ys=3
    if xc in range(a8,b8) and yc in range (yo8-30,yo8-10):
        ys=0
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\commingdown.mp3"))
        yc-=1
    if yc in range(yo9-30,yo9-10) and xc not in range(a9,b9):
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\going up.mp3"))
        ys=3
    if xc in range(a9,b9) and yc in range (yo9-30,yo9-10):
        ys=0
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\commingdown.mp3"))
        yc-=1
    if yc in range(yo10-30,yo10-10) and xc not in range(100,1180):
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\going up.mp3"))
        ys=3
    if xc in range(100,1180) and yc in range (yo10-33,yo10-10):
        ys=0
        game.mixer.Channel(0).play(game.mixer.Sound("sf\\commingdown.mp3"))
        yc-=1
    dis.fill(blue)
    htr=game.Rect(1100,30, 90,70)
    message1("GOAL:HELP THE STICKMAN TO REACH HIS SWEET HEART",ysc)
    game.draw.line(dis,BLACK, [0,yo1],[1280,yo1],10)
    game.draw.line(dis,yellow, [a1,yo1],[b1,yo1],10)
    game.draw.line(dis,BLACK, [0,yo2],[1280,yo2],10)
    game.draw.line(dis,yellow, [a2,yo2],[b2,yo2],10)
    game.draw.line(dis,BLACK, [0,yo3],[1280,yo3],10)
    game.draw.line(dis,yellow, [a3,yo3],[b3,yo3],10)
    game.draw.line(dis,BLACK, [0,yo4],[1280,yo4],10)
    game.draw.line(dis,yellow, [a4,yo4],[b4,yo4],10)
    game.draw.line(dis,BLACK, [0,yo5],[1280,yo5],10)
    game.draw.line(dis,yellow, [a5,yo5],[b5,yo5],10)
    game.draw.line(dis,BLACK, [0,yo6],[1280,yo6],10)
    game.draw.line(dis,yellow, [a6,yo6],[b6,yo6],10)
    game.draw.line(dis,BLACK, [0,yo7],[1280,yo7],10)
    game.draw.line(dis,yellow, [a7,yo7],[b7,yo7],10)
    game.draw.line(dis,BLACK, [0,yo8],[1280,yo8],10)
    game.draw.line(dis,yellow, [a8,yo8],[b8,yo8],10)
    game.draw.line(dis,BLACK, [0,yo9],[1280,yo9],10)
    game.draw.line(dis,yellow, [a9,yo9],[b9,yo9],10)
    game.draw.line(dis,BLACK, [0,yo10],[1280,yo10],10)
    game.draw.line(dis,yellow, [1180,yo10],[100,yo10],10)
    game.draw.line(dis, ash, [0,0],[1280,0], 20)
    game.draw.line(dis, ash, [0,0],[0,720], 20)
    game.draw.line(dis, ash, [0,720],[1280,720], 20)
    game.draw.line(dis, ash, [1280,720],[1280,0], 20)
    draws(dis,xc,yc)
    draws(dis,1200,87)
    dis.blit(ht,(1120,30))
    game.display.flip()
    clock.tick(100)
    if xc in range(1160,1180) and yc in range (0,yo10):
        from textcomponents import heart
        state=True