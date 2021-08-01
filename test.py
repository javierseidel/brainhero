# documentation here

# import image for notes
# hollow image for note to fit in
# scrollling notes right to Left
# frequency range associated with the 5 notes
# if you are within the frequency range, you score the points
# point system
# starting screen

import pygame
import random
import math
from time import sleep
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Brain Hero")
screen = pygame.display.set_mode((1400, 600))


missed_note = pygame.mixer.Sound('sounds/missed_note.wav')
#pygame.mixer.Sound.play(missed_note)

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


game_intro()
#playSong()

open = True


while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
    screen.fill((0, 0, 0))

    keyX -= 12.5
    keyX2 -= 12.5
    keyX3 -= 12.5
    keyX4 -= 12.5
    keyX5 -= 12.5
    screen.blit(pygame.transform.scale(pygame.image.load('images/play_game_background.png'), (1400,600)), (0, 0))
    keysimg(keyX,keyY)
    keysimg2(keyX2,keyY2)
    keysimg3(keyX3,keyY3)
    keysimg4(keyX4,keyY4)
    keysimg5(keyX5,keyY5)
    if keyX == -250:
        keyX = 1400
        keyY = yCoor()
        keysimg(keyX, keyY)

    if keyX2 == -250:
        keyX2 = 1400
        keyY2 = yCoor()
        keysimg2(keyX2, keyY2)

    if keyX3 == -250:
        keyX3 = 1400
        keyY3 = yCoor()
        keysimg3(keyX3,keyY3)

    if keyX4 == -250:
        keyX4 = 1400
        keyY4 = yCoor()
        keysimg4(keyX4,keyY4)

    if keyX5 == -250:
        keyX5 = 1400
        keyY5 = yCoor()
        keysimg5(keyX5,keyY5)


    pygame.display.update()
