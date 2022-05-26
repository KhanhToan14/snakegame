from typing import Tuple
import pygame,random,time, sys

from pygame.constants import K_DOWN

#tạo màn hình console
pygame.init()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((600,400)) #Tạo màn hình
clock = pygame.time.Clock()
#Màu
red = pygame.Color(255,0,0)
#Chèn background
bg = pygame.image.load('background600x400.png').convert()

#Chèn đầu rắn
hsu = pygame.transform.scale(pygame.image.load('headUP.png'),(20,20))
hsd = pygame.transform.scale(pygame.image.load('headD.png'),(20,20))
hsr = pygame.transform.scale(pygame.image.load('headR.png'),(20,20))
hsl = pygame.transform.scale(pygame.image.load('headL.png'),(20,20))
#Chèn đuôi
ts = pygame.transform.scale(pygame.image.load('tailreal.png'),(20,20))
#Chèn food
food = pygame.transform.scale(pygame.image.load('food.png'),(20,20))
#Âm thanh
sound_eat = pygame.mixer.Sound('eat.mp3')
sound_die = pygame.mixer.Sound('die.mp3')
#Các biến
speed = 3
snakepos = [100, 60]
snakebody = [[100,60],[80,60]]
direction = 'RIGHT'
test = 'RIGHT'
foodx = random.randrange(4,56)
foody = random.randrange(4,36)
if foodx % 2 !=0: foodx +=1
if foody %2 != 0: foody +=1
foodpos = [foodx*10, foody*10]
foodflat= True
score = 0
#Hiển thị điểm
def show_score(choice =1):
    sfont=pygame.font.SysFont('none',30)
    sscore=sfont.render('Score: ' + str(score),True, (255,0,0))
    if choice==1:
        screen.blit(sscore,(0,0))
    else:
        screen.blit(sscore,(250,190))

def Game_over():
    gofont = pygame.font.SysFont('none',70)
    sgo=gofont.render('GAME OVER', True, red)
    pygame.mixer.Sound.play(sound_die)
    screen.blit(sgo,(150,140))
    show_score(0)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

    

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                test = 'DOWN'
            elif event.key == pygame.K_UP:
                test = 'UP'
            elif event.key == pygame.K_LEFT:
                test = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                test = 'RIGHT'
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    if test == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    elif test == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif test == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif test == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if direction == 'RIGHT':
        snakepos[0] +=20
    elif direction == "LEFT":
        snakepos[0] -=20
    elif direction == 'UP':
        snakepos[1] -=20
    elif direction == 'DOWN':
        snakepos[1] +=20
    #Rắn dài ra
    snakebody.insert(0,list(snakepos))
    if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
        foodflat = False
        pygame.mixer.Sound.play(sound_eat)
        speed += 0.1
        score += 1
    else:
        snakebody.pop()
    #Respawn food
    if foodflat == False:
        foodx = random.randrange(4,56)
        foody = random.randrange(4,36)
        if foodx % 2 !=0: foodx +=1
        if foody %2 != 0: foody +=1
        foodpos = [foodx*10, foody*10]
    foodflat= True
    #Hiển thị rắn
    screen.blit(bg,(0,0))
    for pos in snakebody:
            screen.blit(ts,(pos[0],pos[1]))
    if direction == 'UP':
        screen.blit(hsu, (snakebody[0][0],snakebody[0][1]))
    if direction == 'DOWN':
        screen.blit(hsd, (snakebody[0][0],snakebody[0][1]))
    if direction == 'RIGHT':
        screen.blit(hsr, (snakebody[0][0],snakebody[0][1]))
    if direction == 'LEFT':
        screen.blit(hsl, (snakebody[0][0],snakebody[0][1]))
    screen.blit(food,(foodpos[0],foodpos[1]))
    if snakepos[0] >580 or snakepos[0] <20:
        Game_over()
    if snakepos[1] >380 or snakepos[1] <20:
        Game_over()
    for x in snakebody[1:]:
        if snakepos[0] == x[0] and snakepos[1] == x[1]:
            Game_over()
    show_score()
    pygame.display.update()
    clock.tick(speed)
