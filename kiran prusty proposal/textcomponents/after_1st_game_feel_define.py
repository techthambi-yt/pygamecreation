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
font_style = pygame.font.SysFont("comicsansms", 20)
def message1(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [1060,680])
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
g=30
while not state:
    x=100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l :
                state = True
    screen.fill((24,3,23))
    text = font.render("Hey its me again... ",True, randomhearts())
    screen.blit(text,[50+s,30+p-g])
    text = font.render("so how do we start this from.... I saw you on the first day of C class...  ",True, randomhearts())
    screen.blit(text,[120+s,70+p-g])
    text = font.render("when i saw you the feeling that hit me was totally different on that day... ",True, randomhearts())
    screen.blit(text,[40+s,80+30+p-g])
    text = font.render("You were such a innocent faced girl to me like you were cute and short so ",True, randomhearts())
    screen.blit(text,[40+s,120+30+p-g])
    text = font.render("it made me to wish of being a friend with you...  ",True, randomhearts())
    screen.blit(text,[40+s,30+160+p-g])
    text = font.render("Next day i got your number ",True, randomhearts())
    screen.blit(text,[780+s,200+30+p-g])
    text = font.render(" ",True,randomtext())
    screen.blit(text,[254+s,200+p-g])
    text = font.render("but i didn't know what to text you about...it was totally new for me because  ",True,randomhearts())
    screen.blit(text,[40+s,30+240+p-g])
    text = font.render("i don't know to start a conversation but i just want to keep in touch with you ",True,randomhearts())
    screen.blit(text,[40+s,30+280+p-g])
    text = font.render("so times passed and we were talking so well... that time i thought of having a  ",True,randomhearts())
    screen.blit(text,[40+s,30+320+p-g])
    text = font.render("sister like you...i wished of having a person to share all the feelings and to ",True,randomhearts())
    screen.blit(text,[40+s,30+360+p-g])
    text = font.render("have little fights with... as days passes by a fear hit me what if after C",True,randomhearts())
    screen.blit(text,[40+s,30+400+p-g])
    text = font.render("we chose different slots and wont be able to talk with each other... because",True,randomhearts())
    screen.blit(text,[40+s,30+440+p-g])
    text = font.render("I know about me that i didn't know what to text you. How many days can i  ",True,randomhearts())
    screen.blit(text,[40+s,30+440+p+40-g])
    text = font.render("i manage with just good morning and good night... but the hardest part was ",True,randomhearts())
    screen.blit(text,[40+s,30+440+p+40+40-g])
    text = font.render("then a week of gap made me miss you soo much and made me realize it was",True,randomhearts())
    screen.blit(text,[40+s,30+40+440+p+40+40-g])
    text = font.render("something else.. I came to see you every possible time I can. But seeing you ",True,randomhearts())
    screen.blit(text,[40+s,30+40+440+p+40+40+40-g])
    text = font.render("just made me miss you soo much.. and now we are here in this conversation....",True,randomhearts())
    screen.blit(text,[40+s,30+40+440+p+40+40+40+40-g])
    message1("press L to continue..........",green)
    pygame.display.flip() 
    clock.tick(60)
    


