import pygame
import random
import math
from pygame import mixer

#Adding Background Sound*******************************************************************************
pygame.mixer.init()
pygame.mixer.music.load('back.wav')
pygame.mixer.music.play()

pygame.init()

#create game window**************************************************************************************
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('Space Shooter Game')
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Adding Background Image********************************************************************************
background=pygame.image.load('background.png')

#Adding Spaceship Image**********************************************************************************
spaceshipimg=pygame.image.load('arcade.png')


alienimg=[]
alienX=[]
alienY=[]
alienspeedX=[]
alienspeedY=[]

#Adding  Alien(Enemy) Image*********************************************************************************
no_of_aliens=15

for i in range(no_of_aliens):
    alienimg.append(pygame.image.load('enemy.png'))
    alienX.append(random.randint(0,736))
    alienY.append(random.randint(30,150))
    alienspeedX.append(-1)
    alienspeedY.append(40)

score=0

#Creating Bullet for Shooting Enemy*****************************************************************************
bulletimg=pygame.image.load('bullet.png')
check=False
bulletX=386
bulletY=490

spaceshipX=370
spaceshipY=480
changeX=0
running=True

font=pygame.font.SysFont('Arial',32,'bold')

#Adding Score********************************************************************************************************
def score_text():
    img=font.render(f'Score:{score}',True,'white')
    screen.blit(img,(10,10))

font_gameover=pygame.font.SysFont('Arial',64,'bold')

#Adding Game Over****************************************************************************************************
def gameover():
    img_gameover = font_gameover.render('GAME OVER', True, 'white')
    screen.blit(img_gameover, (200, 250))






while running:

    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
        #Movement of Spaceship******************************************************************************************
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                changeX=-5
            if event.key==pygame.K_RIGHT:
                changeX=5
            if event.key==pygame.K_SPACE:
                if check is False:
                    bulletSound=mixer.Sound('laser.wav')
                    bulletSound.play()
                    check=True
                    bulletX=spaceshipX+16

        if event.type==pygame.KEYUP:
            changeX=0
    spaceshipX+=changeX  #spaceshipX=spaceshipX-changeX
    if spaceshipX<=0:
        spaceshipX=0
    elif spaceshipX>=736:
        spaceshipX=736
    for i in range(no_of_aliens):
        if alienY[i] > 420:
            for j in range(no_of_aliens):
                alienY[j] = 2000
            gameover()
            break
        #Movement of Alien**********************************************************************************************
        alienX[i]+=alienspeedX[i]
        if alienX[i]<=0:
            alienspeedX[i]=1
            alienY[i]+=alienspeedY[i]
        if alienX[i]>=736:
            alienspeedX[i]=-1
            alienY[i]+=alienspeedY[i]

#Collision Between Bullet and Alien*************************************************************************************
        distance = math.sqrt(math.pow(bulletX - alienX[i], 2) + math.pow(bulletY - alienY[i], 2))
        if distance < 27:
            explosion= mixer.Sound('explosion.wav')
            explosion.play()
            bulletY = 480
            check = False
            alienX[i] = random.randint(0, 736)
            alienY[i] = random.randint(30, 150)
            score += 1
        screen.blit(alienimg[i], (alienX[i], alienY[i]))

    if bulletY<=0:
        bulletY=490
        check=False
    if check:
        screen.blit(bulletimg, (bulletX, bulletY))
        bulletY-=5








    screen.blit(spaceshipimg, (spaceshipX, spaceshipY))
    score_text()
    pygame.display.update()
