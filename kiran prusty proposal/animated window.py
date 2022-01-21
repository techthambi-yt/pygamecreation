import pygame as game
import random
import time
game.init()
game.mixer.music.load("sf\dino1.mp3")
game.mixer.music.play()
randomclr1=(random.randint(0,250),random.randint(0,255),random.randint(0,200))
randomclr=(random.randint(0,250),random.randint(0,255),random.randint(0,200))
randomclr2=(random.randint(0,250),random.randint(0,255),random.randint(0,200))
def message1(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [20, 10])
white=(255,255,255)
dis=game.display.set_mode((1280,720))
game.display.set_caption("letz play")
heartcur=game.image.load("components\\pf\\pink heart.png")
heartcur=game.transform.scale(heartcur,(40,30))
pinkcur=game.image.load("components\\pf\\pink cursor.png")
pinkcur=game.transform.scale(pinkcur,(30,30))
games=game.image.load("components\\pf\\Untitled.png")
games=game.transform.scale(games,(950,250))
snakie1=game.image.load("components\\pf\\snakieee.png")
snakie1=game.transform.scale(snakie1,(400,150))
hp=game.image.load("pf\\heartzpass.png")
hp=game.transform.scale(hp,(450,200))
sh=game.image.load("pf\\sweethearts.png")
sh=game.transform.scale(sh,(260,120))
state=0
win=0
x1=0
y3=89
x2=720
x3=1280
y2=200
y4=550
sw=40
ash=(255,255,255)
randomclr3=(45,78,21)
font_style=game.font.SysFont("comicsansms",35)
tes=font_style.render("I", True, randomclr2)
game.mouse.set_visible(1)
black=(0,0,0)
clock=game.time.Clock()
while not state:
    clock.tick(100)
    for event in game.event.get():
        if event.type==game.QUIT:
            state=1
    dis.fill(black)
    x,y=game.mouse.get_pos()
    pc=game.Rect(x-15,y-15,15,15)
    game.draw.rect(dis,randomclr,(100,x2,10,x1),10)
    game.draw.rect(dis,randomclr1,(250,x1,10,x1),10)
    game.draw.rect(dis,randomclr1,(900,x2,10,x1),10)
    game.draw.rect(dis,randomclr,(1050,x1,10,x1),10)
    game.draw.rect(dis,randomclr3,(780,x1,10,x1),10)
    game.draw.rect(dis,randomclr3,(390,x2,10,x1),10)
    game.draw.line(dis, ash, [0,0],[1280,0], sw)
    game.draw.line(dis, ash, [0,0],[0,720], sw)
    game.draw.line(dis, ash, [0,720],[1280,720], sw)
    game.draw.line(dis, ash, [1280,720],[1280,0], sw)
    dis.blit(games,(150,30))
    dis.blit(snakie1,(420,250))
    dis.blit(hp,(450,400))
    dis.blit(sh,(530,570))
    top=game.Rect(520,270,250,70)
    middle=game.Rect(510,440, 270,90)
    bottom=game.Rect(540,570,230,90)
    if pc.colliderect(top)==0 and pc.colliderect(middle)==0 and pc.colliderect(bottom)==0:
        dis.blit(pinkcur,(x-15,y-15))
    if pc.colliderect(top):
        dis.blit(heartcur,(x-15,y-15))
        if event.type==game.MOUSEBUTTONDOWN:
            from textcomponents import pregame_define
            from components import snakie
            win=1
    if pc.colliderect(middle):
        dis.blit(heartcur,(x-15,y-15))
        if win<1:
            message1("first you should finish the previous level", white)
        if win==1:
            if event.type==game.MOUSEBUTTONDOWN:
                from components import heartpillars
                win=2
    if pc.colliderect(bottom):
        dis.blit(heartcur,(x-15,y-15))
        if win<2:
            message1("first you should finish the previous level", white)
        if win==2:
            if event.type==game.MOUSEBUTTONDOWN:
                from components import sweetheartstickman
                win=3
    if x1==720:
        flag=1
        randomclr=(random.randint(0,100),random.randint(100,255),random.randint(0,200))
        randomclr2=(random.randint(0,250),random.randint(0,255),random.randint(0,200))
        randomclr3=(random.randint(0,250),random.randint(0,205),random.randint(0,205))
        
    if x1==0:
        flag=0
        randomclr1=(random.randint(0,100),random.randint(100,255),random.randint(0,200))
        randomclr2=(random.randint(0,250),random.randint(0,255),random.randint(0,200))
        randomclr3=(random.randint(0,250),random.randint(0,205),random.randint(0,205))
    if flag==0:
        x1+=1.5
        x2-=1.5
        y2=200
    if flag==1:
        x1-=1.5
        x2+=1.5
    if x3==0:
        x3=1280
        y3=random.randrange(0,720,20)
    x3-=2
    game.display.flip()
