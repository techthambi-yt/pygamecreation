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
pygame.mixer.music.load("sf\\fairydust.mp3")
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
            if event.key == pygame.K_u :
                state = True
    screen.fill((24,3,23))
    text = font.render("Happy to see you again.... ",True, randomhearts())
    screen.blit(text,[50+s,30+p])
    text = font.render("its been a pleasure that you hadn't quit the game yet.....  ",True, randomhearts())
    screen.blit(text,[380+s,70+p])
    text = font.render("soo... I really want to ask you out that will you be my first priority in my life  ",True, randomhearts())
    screen.blit(text,[40+s,80+40+p])
    text = font.render("and be my one and only sweet hearted person and give me the opportunity to  ",True, randomhearts())
    screen.blit(text,[40+s,120+40+p])
    text = font.render("be the reason for your smile everyday with happiness and cheer.... ",True, randomhearts())
    screen.blit(text,[40+s,40+160+p])
    text = font.render("Are you willing to accept me as your dream boat  ",True, randomhearts())
    screen.blit(text,[490+s,200+40+p])
    text = font.render(" ",True,randomtext())
    screen.blit(text,[254+s,200+p])
    text = font.render("and trust me with your whole heart to continue the journey of our life",True,randomhearts())
    screen.blit(text,[40+s,40+240+p])
    text = font.render("from this day to the end of our line... I promise that i wont force you or ",True,randomhearts())
    screen.blit(text,[40+s,40+280+p])
    text = font.render("hurt you or make your cry... ",True,randomhearts())
    screen.blit(text,[40+s,40+320+p])
    text = font.render("my only intention is to lead a charming life with ",True,randomhearts())
    screen.blit(text,[490+s,40+390+p-40])
    text = font.render("",True,randomhearts())
    screen.blit(text,[40+s,80+400+p])
    text = font.render("the sweetest person i have ever met.... ",True,randomhearts())
    screen.blit(text,[40+s,80+400+p-40])
    text = font.render("awaiting for your answer..........",True,randomhearts())
    screen.blit(text,[410+s,80+440+p])
    message1("Press U To Continue.....",green)
    pygame.display.flip() 
    clock.tick(60)
    


