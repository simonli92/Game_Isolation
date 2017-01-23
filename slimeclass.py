import pygame
from pygame.locals import *
import random
import math

class slime(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.originalx=x
        self.originaly=y
        self.health=20
        self.attack=5
        self.contain_meat=random.randint(2,3)
        self.defeated=False
        self.disappear=False
        self.image=pygame.image.load("picture/spider.png").convert_alpha()
        self.meat_image=pygame.image.load("picture/meat.png").convert_alpha()
        #picture from game "Don't Starve"
        self.speed=30
        self.count=1

    def drawslime(self,screen):
        if self.disappear==True:
            return
        else:
            if self.health>0:
                screen.blit(self.image,(self.x,self.y))
            else:
                screen.blit(self.meat_image,(self.x,self.y))

    def slime_attack(self,player,time_passed_seconds):
        if self.defeated==False:
            attack_range=((self.x-player.x)**2+(self.y-player.y)**2)**0.5
            if attack_range<200:
                if self.x<player.x+10 and self.y<player.y+15:
                    self.x+=self.speed*time_passed_seconds
                    self.y+=self.speed*time_passed_seconds
                elif self.x<player.x+10 and self.y>player.y+15:
                    self.x+=self.speed*time_passed_seconds
                    self.y-=self.speed*time_passed_seconds
                elif self.x>player.x+10 and self.y<player.y+15:
                    self.x-=self.speed*time_passed_seconds
                    self.y+=self.speed*time_passed_seconds
                elif self.x>player.x+10 and self.y>player.y+15:
                    self.x-=self.speed*time_passed_seconds
                    self.y-=self.speed*time_passed_seconds
                if  self.counter_touch(player):
                    self.count+=1
                    if self.count==40:
                        player.health-=self.attack
                        player.being_attacked=True
                        self.count=1
                    elif self.defeated==True or self.count<40:
                        player.being_attacked=False

    def counter_touch(self,player):
        if (self.x>player.x-10 and self.x<player.x+40 and
            self.y>player.y-60 and self.y<player.y+80):
            return True
                    
                

    
            
            
            
