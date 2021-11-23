# import the pygame module, so you can use it
import pygame
import math
import os
import random
from pygame.locals import *
from creature import creature

 # initialize the pygame module
pygame.display.init()
pygame.font.init()
# load and set the logo
pygame.display.set_caption("Evolution")

# create window
window = pygame.display.set_mode((1280,720))
baba_Texture = pygame.image.load(os.path.join('images','baba.png'))
baba = creature((640,360),baba_Texture)

food_Texture = pygame.image.load(os.path.join('images','apple.png'))
foodCoords = []

def generateFood():
    for i in range(15):
        foodCoords.append((random.randrange(1280),random.randrange(720)))


def main():
    # define a variable to control the main loop
    running = True
    black = (0,0,0)
    generateFood()

    # main loop
    while running:
        if baba.state != 0:
            baba.updatePosFromQueue()
        pygame.event.get()
        pygame.display.flip()
        window.fill(black)
        babaX = baba.pos[0]
        babaY = baba.pos[1]
        for i in foodCoords:
            if i[0] < babaX+16 and i[0] > babaX-16 and i[1] < babaY+16 and i[1] > babaY-16:
                foodCoords.remove(i)
            else:
                window.blit(food_Texture,(i[0]-16,i[1]-16))
        window.blit(baba.sprite,(babaX-24,babaY-24))
        if baba.state == 0 and len(foodCoords) >= 1:
            closestFoodCoords = baba.findNearest(foodCoords)
            baba.moveToPoint(closestFoodCoords[0],closestFoodCoords[1])



        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    generateFood()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                baba.moveToPoint(x,y)
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pygame.quit()

if __name__ == '__main__':
    main()
