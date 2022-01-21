import pygame as game
import random
import time as tm
game.init()
game.mixer.init()
hearts=game.image.load("pf\ht1.png")
game.display.set_icon(hearts)
hearts=game.transform.scale(hearts,(70,70))
dis=game.display.set_mode((1280,720))
clock=game.time.Clock()
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
    dis.blit(mesg, [450,300])
def message4(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [500,370])
black=(0,0,0)
r=(255,0,0)
ys=(5,205,5)
font_style = game.font.SysFont("comicsansms", 30)
def q():
    game.quit()
def gameloop():
    game.mixer.music.load("sf\\dino.mp3")
    win=0
    game.mixer.music.play()
    red=(25,255,45)
    game_close=False
    re=(35,4,235)
    whit=(255,255,255)
    white=(25,25,25)
    u=1
    time=0
    yy=530
    s=1
    ts=0
    p=1
    j=1
    k=1
    aa=100
    bb=0
    dd=550
    sd2=-(720-530-90)
    cc=400
    su=160
    sd=-(720-160-90)
    sd1=530
    game.mouse.set_visible(0)
    state=0
    while not state:
        clock.tick(400)     
        game_close=False               
        for event in game.event.get():
            if event.type==game.QUIT:
                state=1
        if s==1280:
            bb=random.randrange(50,100,10)
            su=random.randrange(200,600,20)
            s=0
        if p==1280+aa:
            aa=random.randrange(50,100,10)
            sd=-(720-su-90)
            p=0    
        if j==1280+cc:
            cc=random.randrange(120,200,10)
            sd1=random.randint(20,600)
            j=0    
        if k==1280+dd:
            dd=random.randrange(200,300,10)
            sd2=-(720-sd1-90)
            k=0
        if u==1280:
            yy=random.randint(200,600)
            u=0
        x,y=game.mouse.get_pos()
        cur=game.Rect(x,y+15,6,6)
        dis.fill(white)
        message1("GOAL: survive for 69 seconds", ys)
        dis.blit(hearts,(x,y))
        up=game.Rect(1280-s+bb,0,30,su-8)
        down=game.Rect(1280-p+aa,720,30,sd+8)
        up1=game.Rect(1200-j+cc,0,30,sd1-8)
        down1=game.Rect(1150-k+dd,720,30,sd2+8)
        coin=game.Rect(1280-u,yy,20,20)
        game.draw.rect(dis,whit,up1,5)
        game.draw.rect(dis,r,up,8)
        game.draw.rect(dis,whit,down,5)
        game.draw.rect(dis,r,down1,8)
        game.draw.rect(dis,ys,coin,5)
        game.draw.rect(dis,ys,coin,5)
        s=s+1
        message3("time survived : "+str(ts),ys)
        u+=1
        nkg=10
        p=p+1
        j+=1
        k+=1
        time+=1
        ts=time/100
        game.display.update()
        if  cur.colliderect(up) or cur.colliderect(down) or cur.colliderect(up1) or cur.colliderect(down1):
            game_close=True
        if ts == 69.69:
            win=1
            from textcomponents import after_heartz_pillar
            game_close=False   
            state=True
            game.mixer.music.stop()
            break         
        while game_close == True:
            dis.fill((45,8,45))           
            nk=random.randint(100,255)
            rc=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
            game.draw.rect(dis,rc, [230,240,500+370,130+70],10)
            message("WANNA PLAY AGAIN.", whit)
            message4("HAPPINESS IS WATCHING YOU SMILE ",(nkg,nk-10,nk))
            message2("PRESS Y TO PLAY AGAIN ", whit)
            game.display.update()
            nkg+=20
            if nkg>250:
                nkg=0
            tm.sleep(0.2)
            for event in game.event.get():
                if event.type==game.QUIT:
                    state=True
                    game_close = False
                       # game.quit()
                if event.type==game.KEYDOWN:
                    if event.key == game.K_y:
                        state=True
                        game_close=False
                        gameloop()    
gameloop()

