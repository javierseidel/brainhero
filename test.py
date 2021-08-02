# documentation here


# hollow image for note to fit in

# frequency range associated with the 5 notes
# if you are within the frequency range, you score the points
# point system
# starting screen

import pygame
import random
import math
from time import sleep
from pygame.locals import *
import csv
from csv import DictReader
import time




pygame.init()
pygame.display.set_caption("Brain Hero")
screen = pygame.display.set_mode((1400, 600))
rect_hit_note1 = pygame.Rect(397,185,5,30)
rect_hit_note2 = pygame.Rect(397,215,5,30)
rect_hit_note3 = pygame.Rect(397,245,5,30)
rect_hit_note4 = pygame.Rect(397,275,5,30)
rect_hit_note5 = pygame.Rect(397,305,5,30)

missed_note = pygame.mixer.Sound('sounds/missed_note.wav')
#pygame.mixer.Sound.play(missed_note)

read_obj = csv.reader(open('Data/data.csv', 'r'))
def readData(read_obj):

    for row in read_obj:
        for x in row:
            if 15 <= abs(int(float(x))) <= 30:
                pygame.draw.rect(screen, RED, rect)
            elif 30 < abs(int(float(x))) <= 45:
                return 4
            elif 45 < abs(int(float(x))) <= 60:
                return 3
            elif 60 < abs(int(float(x))) <= 75:
                return 2
            elif 75 < abs(int(float(x))):
                return 1

# plays a curated song
def playSong():
    pygame.mixer.init()
    pygame.mixer.Sound.play(pygame.mixer.Sound('sounds/schoolsout.mp3'))

# implementation for white text objects
def text_objects(text, font):
    white = (255, 255, 255)
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

#prints image
def keysimg(x, y):
    keyimg = pygame.image.load('images/blue_line.png')
    keyimg1 = pygame.transform.scale(keyimg, (300,300))

    return screen.blit(keyimg1, (x,y))

def keysimg2(x, y):
    keyimg2 = pygame.image.load('images/blue_line.png')
    keyimg2_1 = pygame.transform.scale(keyimg2, (300,300))
    return screen.blit(keyimg2_1, (x,y))

def keysimg3(x, y):
    keyimg3 = pygame.image.load('images/blue_line.png')
    keyimg3_1 = pygame.transform.scale(keyimg3, (300,300))
    return screen.blit(keyimg3_1, (x,y))

def keysimg4(x, y):
    keyimg4 = pygame.image.load('images/blue_line.png')
    keyimg4_1 = pygame.transform.scale(keyimg4, (300,300))
    return screen.blit(keyimg4_1, (x,y))

def keysimg5(x, y):
    keyimg5 = pygame.image.load('images/blue_line.png')
    keyimg5_1 = pygame.transform.scale(keyimg5, (300,300))
    return screen.blit(keyimg5_1, (x,y))


# randomizes y coordinate for image
def yCoor():
    full_chord = random.randint(1,5)
    if full_chord == 1:
        return 127

    elif full_chord == 2:
        return 150

    elif full_chord == 3:
        return 175

    elif full_chord == 4:
        return 205

    else:
        return 230

def collision_detect(x):
    if x.colliderect(rect):
        pygame.draw.rect(screen, GRAY, rect)
    elif x.colliderect(rect2):
        pygame.draw.rect(screen, GRAY, rect2)
    elif x.colliderect(rect3):
        pygame.draw.rect(screen, GRAY, rect3)
    elif x.colliderect(rect4):
        pygame.draw.rect(screen, GRAY, rect4)
    elif x.colliderect(rect5):
        pygame.draw.rect(screen, GRAY, rect5)

# starting screen
def game_intro():
    bright_green = (0, 204, 0)
    green = (0, 255, 0)

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        background = pygame.image.load('images/guitarherobackground.png')
        new_background = pygame.transform.scale(background, (1400,600))
        screen.blit(new_background, (0,0))
        largeText = pygame.font.Font('freesansbold.ttf',30)
        TextSurf, TextRect = text_objects("Brain Hero", largeText)
        TextRect.center = ((1400 / 2),(600 / 2))
        screen.blit(TextSurf, TextRect)


        mouse = pygame.mouse.get_pos()

        click = pygame.mouse.get_pressed()

        #print(mouse)

        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(screen, bright_green,(150,450,100,50))
            if click[0] == 1:
                break
                mainGame()
            else:
                pygame.draw.rect(screen, green,(150,450,100,50))
        pygame.display.update()
# main
def mainGame():
    clock = pygame.time.Clock()

    while mainGame:
        for event in pygame.event.get():
                #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

                background1 = pygame.image.load('images/play_game_background.png')
                new_background1 = pygame.transform.scale(background1, (1400,600))
                screen.blit(new_background1, (0,0))
        pygame.display.update()


keyX = 1500
keyY = yCoor()

keyX2 = 1800
keyY2 = yCoor()

keyX3 = 2100
keyY3 = yCoor()

keyX4 = 2400
keyY4 = yCoor()

keyX5 = 2700
keyY5 = yCoor()

RED = (255, 0, 0)
GRAY =(0, 0, 0)




v = [-10, 0]

game_intro()
#playSong()

open = True


while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
    screen.fill((0, 0, 0))

    readData(read_obj)

    keyX -= 10
    keyX2 -= 10
    keyX3 -= 10
    keyX4 -= 10
    keyX5 -= 10
    screen.blit(pygame.transform.scale(pygame.image.load('images/play_game_background.png'), (1400,600)), (0, 0))

    keysimg(keyX,keyY)
    rect = pygame.Rect(keyX, (keyY+60), 300, 30)
    rect.move_ip(v)


    keysimg2(keyX2,keyY2)
    rect2 = pygame.Rect(keyX2, (keyY2+60), 300, 30)
    rect2.move_ip(v)
    pygame.draw.rect(screen, RED, rect2)

    keysimg3(keyX3,keyY3)
    rect3 = pygame.Rect(keyX3, (keyY3+60), 300, 30)
    rect3.move_ip(v)
    pygame.draw.rect(screen, RED, rect3)

    keysimg4(keyX4,keyY4)
    rect4 = pygame.Rect(keyX4, (keyY4+60), 300, 30)
    rect4.move_ip(v)
    pygame.draw.rect(screen, RED, rect4)

    keysimg5(keyX5,keyY5)
    rect5 = pygame.Rect(keyX5, (keyY5+60), 300, 30)
    rect5.move_ip(v)
    pygame.draw.rect(screen, RED, rect5)

    pygame.draw.rect(screen, RED, rect_hit_note1)
    pygame.draw.rect(screen, RED, rect_hit_note2)
    pygame.draw.rect(screen, RED, rect_hit_note3)
    pygame.draw.rect(screen, RED, rect_hit_note4)
    pygame.draw.rect(screen, RED, rect_hit_note5)

    if keyX == -250:
        keyX = 1400
        keyY = yCoor()
        keysimg(keyX, keyY)

    if rect.right < 0:
        rect.left = 1400
    pygame.display.flip()
    pygame.display.update()

    if keyX2 == -250:
        keyX2 = 1400
        keyY2 = yCoor()
        keysimg2(keyX2, keyY2)

    if rect2.right < 0:
        rect2.left = 1400
    pygame.display.flip()
    pygame.display.update()

    if keyX3 == -250:
        keyX3 = 1400
        keyY3 = yCoor()
        keysimg3(keyX3,keyY3)

    if rect3.right < 0:
        rect3.left = 1400
    pygame.display.flip()
    pygame.display.update()

    if keyX4 == -250:
        keyX4 = 1400
        keyY4 = yCoor()
        keysimg4(keyX4,keyY4)

    if rect4.right < 0:
        rect4.left = 1400
    pygame.display.flip()
    pygame.display.update()


    if keyX5 == -250:
        keyX5 = 1400
        keyY5 = yCoor()
        keysimg5(keyX5,keyY5)

    if rect5.right < 0:
        rect5.left = 1400
    pygame.display.flip()
    pygame.display.update()

    collision_detect(rect_hit_note1)
    collision_detect(rect_hit_note2)
    collision_detect(rect_hit_note3)
    collision_detect(rect_hit_note4)
    collision_detect(rect_hit_note5)






    pygame.display.update()
