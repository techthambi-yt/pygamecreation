import pygame,random,time
pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue =(0, 0, 225)
lightblue=(153,204,255)
dodgerblue=(30,144,255)
deepskyblue=(0,191,255)
hotpink=(255,105,180)
deeppink=(255,20,147)
pink=(255,192,203)
yellow=(255,255,0)
p=0
s=0
font_style = pygame.font.SysFont("comicsans", 30)
def message1(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [950, 650])
pygame.mixer.music.load("sf//fairydust.mp3")
pygame.mixer.music.play()
size = (1280,720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PROPOSAL PROGRAM")
def randomhearts():
    rana=(red,hotpink,deeppink,pink)
    heartcol=random.choice(rana)
    return (heartcol)
def randomtext():
    textcol=(random.randint(0,100),random.randint(100,255),random.randint(0,200))
    time.sleep(.5)
    return (textcol)
state=False
clock = pygame.time.Clock()
font = pygame.font.Font(None,60)
a="love"
while not state:
    x=100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c :
                state = True
    screen.fill((24,3,23))
    text = font.render(a,True, randomhearts())
    screen.blit(text,[150+s,0+p])
    text = font.render(a,True, randomhearts())
    screen.blit(text,[450+s,0+p])
    text = font.render(a*2,True, randomhearts())
    screen.blit(text,[120+s,40+p])
    text = font.render(a*2,True, randomhearts())
    screen.blit(text,[400+s,40+p])
    text = font.render(a*7,True, randomhearts())
    screen.blit(text,[60+s,80+p])
    text = font.render(a*8,True, randomhearts())
    screen.blit(text,[20+s,120+p])
    text = font.render(a*8,True, randomhearts())
    screen.blit(text,[20+s,160+p])
    text = font.render(a*2,True, randomhearts())
    screen.blit(text,[50+s,200+p])
    text = font.render("  -Kutti devil- ",True,randomtext())
    screen.blit(text,[214+s,200+p])
    text = font.render(a*2,True,randomhearts())
    screen.blit(text,[490+s,200+p])
    text = font.render(a*6,True,randomhearts())
    screen.blit(text,[100+s,240+p])
    text = font.render(a*5,True,randomhearts())
    screen.blit(text,[140+s,280+p])
    text = font.render(a*4,True,randomhearts())
    screen.blit(text,[177+s,320+p])
    text = font.render(a*3,True,randomhearts())
    screen.blit(text,[220+s,360+p])
    text = font.render(a*2,True,randomhearts())
    screen.blit(text,[260+s,400+p])
    text = font.render(a,True,randomhearts())
    screen.blit(text,[300+s,440+p])
    
    text = font.render("I love you",True,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    screen.blit(text,[250+s,500+p])
    if s>70 and s<140:
        p-=10
        s+=5
    elif s>210 and s<280:
        p-=10
        s+=5
    elif s>350 and s<420:
        p-=10
        s+=5
    elif s>490 and s<560:
        p-=10
        s+=5
    elif s>630 and s<700:
        p-=10
        s+=5
    else:
        p+=10
        s+=5 
    message1("Press C To Continue.....",green)
    pygame.display.flip() 
    clock.tick(60)
    


