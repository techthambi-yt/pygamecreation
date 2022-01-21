import pygame
import time
import random
pygame.init()
sc=0
q=5
#colour codes 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (30, 13, 23)
dark_blue=(167, 16, 25)
ash=(25,255,55)
ys=(5,205,5)
ed=(80,60,70)
fi=(45,76,90)
#display area
dis_width = 1280
pygame.mouse.set_visible(0)
dis_height = 720
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('snakie')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 20
font_style = pygame.font.SysFont("comicsansms", 30)
score_font = pygame.font.SysFont("comicsansms", 35)
def Your_score(score):
    value = score_font.render("Your score: " + str(score*5), True, ys)
    dis.blit(value, [900,30])
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, dark_blue, [x[0], x[1], snake_block+q, snake_block+q])
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
def gameLoop():
    sw=10
    pygame.mixer.music.load("sf\dino4.mp3")
    pygame.mixer.music.play()
    state=0
    hstate=1
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    nkg=0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block+q) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block+q) / 10.0) * 10.0
    while not game_over:
        fi=(random.randint(50,250),random.randint(1,5),random.randint(50,210))
        while game_close == True:
            dis.fill(ed)         
            nk=random.randint(100,255)
            rc=(random.randint(70,255),random.randint(70,255),random.randint(70,255))
            pygame.draw.rect(dis,rc, [230,240,500+370,130+70],10)
            message("WANNA PLAY AGAIN.", white)
            message4("SOMETIMES IT IS OK NOT TO BE OK ",(nkg,nk-10,nk))
            message2("PRESS Y TO PLAY AGAIN ", white)
            pygame.display.update()
            time.sleep(0.1)  
            nkg+=20
            if nkg>250:
                nkg=0
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                     game_over = True
                     game_close = False
                     pygame.mixer.music.stop()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        game_over = True
                        game_close = False
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.line(dis, ash, [0,0],[1280,0], sw)
        pygame.draw.line(dis, ash, [0,0],[0,720], sw)
        pygame.draw.line(dis, ash, [0,720],[1280,720], sw)
        pygame.draw.line(dis, ash, [1280,720],[1280,0], sw)
        for pl in range(1,1000):
         if (pl%2==1):
            pygame.draw.rect(dis, green, [foodx, foody, snake_block+q, snake_block+q],5)
           #pygame.draw.rect(dis,yellow, [foodx, foody, snake_block+q, snake_block+q],1)
            #pygame.draw.rect(dis,red, [foodx+1, foody+1, snake_block+q-2, snake_block+q-2])
         else:
             pygame.draw.rect(dis, black, [foodx, foody, snake_block+q, snake_block+q],5)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        message1("GOAL:score 100 points", ys)
        Your_score(Length_of_snake - 1)
        sc=(Length_of_snake-1)/2
        if sc==5*2:
            game_over=True
            hstate=0
        pygame.display.update()
        if x1 == foodx and y1 == foody :
            pygame.mixer.Channel(0).play(pygame.mixer.Sound("sf/point.mp3"))
            foodx = round(random.randrange(0, dis_width - snake_block+q) / 20.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block+q) / 20.0) * 10.0
            Length_of_snake += 2
        elif x1 == foodx+10 and y1 == foody+10 :
            pygame.mixer.Channel(0).play(pygame.mixer.Sound("sf/point.mp3"))
            foodx = round(random.randrange(0, dis_width - snake_block+q) / 20.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block+q) / 20.0) * 10.0
            Length_of_snake += 2
        elif x1 == foodx-10 and y1 == foody-10 :
            pygame.mixer.Channel(0).play(pygame.mixer.Sound("sf/point.mp3"))
            foodx = round(random.randrange(0, dis_width - snake_block+q) / 20.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block+q) / 20.0) * 10.0
            Length_of_snake += 2
        clock.tick(snake_speed)
    if sc==5*2:
        while not hstate:
            from textcomponents import after_1st_game_feel_define
            hstate=1
gameLoop()
