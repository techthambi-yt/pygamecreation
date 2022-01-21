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
font_style = pygame.font.SysFont("comicsansms", 30)
def message1(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [950,620])
pygame.mixer.music.load("fairydust.mp3")
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
font = pygame.font.SysFont("comicsansms",35)
a="love"
while not state:
    x=100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i :
                state = True
    screen.fill((24,3,23))
    text = font.render("Hey Kiran...",True, randomhearts())
    screen.blit(text,[50+s,30+p])
    text = font.render("its been a week or two since we completed our c programing course... ",True, randomhearts())
    screen.blit(text,[120+s,70+p])
    text = font.render("or should i say it's been 2 weeks filled with of days missing you like crazy....",True, randomhearts())
    screen.blit(text,[40+s,80+40+p])
    text = font.render("i thought of having a friend or a sister in you... but now i realised that there ",True, randomhearts())
    screen.blit(text,[40+s,120+40+p])
    text = font.render("was something more in this...... ",True, randomhearts())
    screen.blit(text,[40+s,40+160+p])
    text = font.render("I dont know how you will take this but from ",True, randomhearts())
    screen.blit(text,[530+s,200+35+p])
    text = font.render(" ",True,randomtext())
    screen.blit(text,[254+s,200+p])
    text = font.render("the end of our c course i was waiting to tell you this...",True,randomhearts())
    screen.blit(text,[40+s,40+240+p])
    text = font.render("I think now it is the time to end all that fears and ask you out..... but there ",True,randomhearts())
    screen.blit(text,[40+s,80+280+p])
    text = font.render("hits my problem! i am not that good in talking with girls in personal!!! ",True,randomhearts())
    screen.blit(text,[40+s,80+320+p])
    text = font.render("but i know i can write a program of one or two lines to make this happen...  ",True,randomhearts())
    screen.blit(text,[40+s,80+360+p])
    text = font.render("",True,randomhearts())
    screen.blit(text,[40+s,80+400+p])
    text = font.render("i hope it wont make you bored, at least for a minute or so.....",True,randomhearts())
    screen.blit(text,[210+s,80+440+p])
    message1("Press I To Continue.....",green)
    pygame.display.flip() 
    clock.tick(60)
    


