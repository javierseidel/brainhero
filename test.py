# documentation here
# "Brain Hero"
# import a background, dynamic background if time
# import song- schools out alice cooper
# import image for notes
# hollow image for note to fit in
# scrollling notes right to Left
# frequency range associated with the 5 notes
# if you are within the frequency range, you score the points
# point system

import pygame
from pygame.locals import *

pygame.init()

pygame.display.set_caption("Brain Hero")

screen=pygame.display.set_mode((1400, 600))

while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
