
from collections import deque
import math
import pygame

class creature:

##    coordinate system:
##
##   (0,0)                   (1280,0)
##    |----------------------->
##    |
##    |
##    |
##    |
##    V
##  (0,720)

## states:
## 0 = still
## 1 = moving

    def __init__(self,coords,texture):
         self.pos = coords
         self.speed = 1
         self.state = 0
         self.moveQueue = deque()
         self.sprite = texture
         self.rightSprite = texture
         self.leftSprite = pygame.transform.flip(texture, True, False)


    def updatePosFromQueue(self):
        if len(self.moveQueue) == 0:
            self.state = 0
        else:
            newCoords = self.moveQueue.pop()
            self.pos = (newCoords[0],newCoords[1])
            if len(self.moveQueue) == 0:
                self.state = 0
            
    def distToPoint(self,coords):
        x1 = coords[0]
        y1 = coords[1]
        return math.sqrt(math.pow((x1-self.pos[0]),2) + math.pow((y1-self.pos[1]),2))

    def findNearest(self,listOfCoords):
        closestDist = 0
        closestCoords = listOfCoords[0]
        for x in listOfCoords:
            distToPoint = self.distToPoint(x)
            if distToPoint < closestDist:
                closestDist = distToPoint
                closestCoords = x
        return closestCoords

    def moveToPoint(self,x,y):
        dX = x-self.pos[0]
        dY = y-self.pos[1]
        if dX == 0 and dY == 0:
            self.state = 0
        else:
            if len(self.moveQueue) > 0:
                self.moveQueue.clear()
            if x < self.pos[0]:
                self.sprite = self.leftSprite
            else:
                self.sprite = self.rightSprite
            self.state = 1
            dist = math.sqrt(math.pow(dX,2) + math.pow(dY,2))
            turns = int(dist/self.speed)
            if dist%self.speed != 0:
                turns += 1
            for i in range(turns+1):
                if i > 0:
                    if i == turns:
                        self.moveQueue.appendleft((x,y))
                    else:
                        self.moveQueue.appendleft((self.pos[0]+(i*(dX/turns)),self.pos[1]+(i*(dY/turns))))
