

import pygame
import random
import math
from  pygame import mixer


# initalizes pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 700))


# background
background = pygame.image.load('background.jpg')

# music
mixer.music.load("Treefingers.mp3")
mixer.music.play(-1)


# title and icon
pygame.display.set_caption("Protect the Aliens")


# player
playerImg = pygame.image.load('alien.png')
playerX = 370
playerY = 635
playerX_change = 0

# lives

num_lives = 3



enemies_down = 0
   


# enemy arraylist created and appended
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change =[]
num_of_enemies = 15

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(-600, 650))
    enemyX_change.append(2)
    enemyY_change.append(60)



# defense
# Ready - you cant see the bullet on the screen
# Fire - bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 570
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

# score
score_value=0
font = pygame.font.Font('freesansbold.ttf', 32)

# game over font
over_font = pygame.font.Font('freesansbold.ttf', 62)



textX = 10
textY = 10
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x,y))

def game_over_text():
    game_over = over_font.render("GAME OVER press any button to exit and e to play again" , True, (255, 255, 255))
    screen.blit(game_over, (275,250))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    global num_lives
                    global enemies_down
                    global score_value
                    num_lives = 3
                    enemies_down = 0
                    score_value=0
                   
                    for i in range(15):
                        
                        enemyX[i] = random.randint(0, 735)
                        enemyY[i] = random.randint(-600, 650)
                        enemyX_change[i] = 2
                        enemyY_change[i] = 60
                    
                    


        
        

# live

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y+10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2)+math.pow(enemyY - bulletY, 2))
    if distance < 27 and bullet_state == "fire":
        return True
    else:
        return False

def captured(enemyX, enemyY, playerX, playerY):
    distancee = math.sqrt(math.pow(enemyX-playerX, 2)+math.pow(enemyY - playerY, 2))
    if distancee < 27:
        return True
    else:
        return False
running = True
game_over = False
while running:
        screen.fill((0, 0, 0))
        # background image
        screen.blit(background, (0, 0))

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0


        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

    

        
        # enemy movement
        for i in range(num_of_enemies):
            # game over
        
            
            if captured(enemyX[i], enemyY[i], playerX, playerY):
                num_lives -= 1
                enemyY[i] = 2000

            if num_lives == 0:
                for i in range(num_of_enemies):
                    enemyY[i] = 2000

                game_over = True         
            
                        
              
                

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 2
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -2
                enemyY[i] += enemyY_change[i]

            # collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 600
                bullet_state = "ready"
                score_value += 1
                enemies_down += 1
                print(score_value)
                
                enemyY[i] = 2000

            enemy(enemyX[i], enemyY[i], i)


        if num_lives == 3:
            screen.blit(pygame.image.load("life.png"), (750, 15))
            screen.blit(pygame.image.load('life.png'), (700, 15))
            screen.blit(pygame.image.load('life.png'), (650, 15))
        if num_lives == 2:
            screen.blit(pygame.image.load('life.png'), (750, 15))
            screen.blit(pygame.image.load('life.png'), (700, 15))
        if num_lives == 1:
            screen.blit(pygame.image.load('life.png'), (750, 15))
        if num_lives == 0:
            heartless = font.render("You have no lives left. ", True, (255, 255, 255))
            screen.blit(heartless, (600, 20))

            
        # bullet movement
        if bulletY <= 0:
            bulletY = 570
            bullet_state = "ready"
        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        


        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()

    


                        
            
