import pygame
from pygame.locals import *
import random

class tree(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.originalx=x
        self.originaly=y
        self.height=120
        self.width=80
        self.health=10
        self.contain=random.randint(2,3)
        self.tree_image=pygame.image.load("picture/tree.png").convert_alpha()
        self.wood_image=pygame.image.load("picture/wood.png").convert_alpha()
        #picture from game "Don't Starve"
        self.disappear=False

    def drawtree(self,screen):
        if self.disappear==True:
            return
        else:
            if self.health>0:
                screen.blit(self.tree_image,(self.x,self.y))
            else:
                screen.blit(self.wood_image,(self.x,self.y+self.height-20))

    def collided(self,other):
        if (other.x>self.x-30 and other.x<self.x+self.width and
            other.y<self.y+self.height and other.y>self.y-self.height/2):
            return True

   
class grass(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.originalx=x
        self.originaly=y
        self.height=70
        self.width=50
        self.health=10
        self.contain=random.randint(2,3)
        self.grass_image=pygame.image.load("picture/grass.png").convert_alpha()
        self.cutgrass_image=pygame.image.load("picture/cutgrass.png").convert_alpha()
        #picture from game "Don't Starve"
        self.disappear=False
        

    def drawgrass(self,screen):
        if self.disappear==True:
            return
        else:
            if self.health>0:
                screen.blit(self.grass_image,(self.x,self.y))
            else:
                screen.blit(self.cutgrass_image,(self.x,self.y+30))

    def collided(self,other):
        if (other.x>self.x-self.width and other.x<self.x+self.width and
            other.y<self.y+self.height and other.y>self.y-self.height):
            return True

    

class berry_tree(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.originalx=x
        self.originaly=y
        self.height=80
        self.width=30
        self.contain=random.randint(1,2)
        self.add_status=(10,20,5)
        self.berrytree_image=pygame.image.load("picture/berry_tree.png").convert_alpha()
        self.berrytreeno_image=pygame.image.load("picture/berry_tree_noberry.png").convert_alpha()
        #picture from game "Don't Starve"
        self.disappear=False

    def drawberry(self,screen):
        if self.disappear==True:
            screen.blit(self.berrytreeno_image,(self.x,self.y)) 
        else:
            screen.blit(self.berrytree_image,(self.x,self.y))
            

    def collided(self,other):
        if (other.x>self.x-self.width and other.x<self.x+self.width and
            other.y<self.y+self.height/2 and other.y>self.y-self.height/4):
            return True

class stone(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.originalx=x
        self.originaly=y
        self.height=80
        self.width=100
        self.health=10
        self.contain=random.randint(2,3)
        self.stone_image=pygame.image.load("picture/stone.png").convert_alpha()
        self.stonecut_image=pygame.image.load("picture/stone_cut.png").convert_alpha()
        #picture from game "Don't Starve"
        self.disappear=False
        

    def drawstone(self,screen):
        if self.disappear==True:
            return
        else:
            if self.health>0:
                screen.blit(self.stone_image,(self.x,self.y))
            else:
                screen.blit(self.stonecut_image,(self.x+self.width/4,self.y+23))

    def collided(self,other):
        if (other.x>self.x-30 and other.x<self.x+self.width and
            other.y<self.y+self.height/2 and other.y>self.y-self.height/4):
            return True


class wormhole(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.originalx=x
        self.originaly=y
        self.image=pygame.image.load("picture/wormhole.png")
        #picture from game "Don't Starve"

    def drawwormhole(self,screen):
        screen.blit(self.image,(self.x,self.y))


    def collided(self,other):
        if (other.y+90<self.y+40 and other.y+90>self.y and
            other.x+45<self.x+60 and other.x+45>self.x):
            return True
        




    
