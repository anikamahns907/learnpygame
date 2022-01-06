

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

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change =[]
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(5)
    enemyY_change.append(40)

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


over_font = pygame.font.Font('freesansbold.ttf', 32)


textX = 10
textY = 10
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x,y))

def game_over_text():
    game_over = font.render("GAME OVER" , True, (255, 255, 255))
    screen.blit(game_over, (250,200))

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y+10))


def isCollision(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x1-x2, 2)+math.pow(y1 - y2, 2))
    if distance < 10:
        return True
    else:
        return False



 

    # game loop
running = True
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
        if isCollision(enemyY[i], enemyX[i], playerX, playerY):
            for i in range(num_of_enemies):
                enemyY[i] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -5
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 600
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)


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
