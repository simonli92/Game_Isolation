import pygame
from pygame.locals import *
import random
import  treeclass
import slimeclass

    
class player1(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.originalx=x
        self.originaly=y
        self.health=100
        self.hunger=101
        self.spirit=100
        self.bag=dict()
        self.bag_list=[]
        self.attack=10
        self.gameover=False
        self.front=pygame.image.load("picture/frontman_nohat.png").convert_alpha()
        self.right=pygame.image.load("picture/right_nohat.png").convert_alpha()
        self.left=pygame.image.load("picture/left_nohat.png").convert_alpha()
        self.back=pygame.image.load("picture/back_nohat.png").convert_alpha()
        #picture from game "Don't Starve"
        self.speed=[0,0]
        self.event_pickup=False
        self.attack_status=False
        self.being_attacked=False
        self.eating=False
        self.equip_bag=[None]*4
        self.open_craft=[False]*5
        self.equip_fire=False
        self.equip_woodsword=False
        self.equip_stonesword=False
        self.open_pot=False
        self.pot_contain=[None]*4
        self.drag_food=False
        self.food_inmouse=False
        self.cook_status=False
        self.teleport_status=False
        self.teleport_count=1
        self.ggcount=1
        self.maxx=self.originalx/10+330+20
        self.maxy=self.originaly/10+220+30
        self.leastx=self.originalx/10+330-10
        self.leasty=self.originaly/10+220-10
        self.walkcount=0
        self.walk1=pygame.image.load("picture/frontman_nohat_walk.png").convert_alpha()
        self.walk2=pygame.image.load("picture/frontman_nohat_walk2.png").convert_alpha()
        self.backwalk1=pygame.image.load("picture/back_nohat_walk.png").convert_alpha()
        self.backwalk2=pygame.image.load("picture/back_nohat_walk2.png").convert_alpha()
        self.leftwalk1=pygame.image.load("picture/left_nohat_walk.png").convert_alpha()
        self.rightwalk1=pygame.image.load("picture/right_nohat_walk.png").convert_alpha()
        self.frontattack=pygame.image.load("picture/frontman_nohat_attack.png").convert_alpha()
        self.leftattack=pygame.image.load("picture/left_nohat_attack.png").convert_alpha()
        self.rightattack=pygame.image.load("picture/right_nohat_attack.png").convert_alpha()
        self.backattack=pygame.image.load("picture/back_nohat_attack.png").convert_alpha()
        #picture from game "Don't Starve"
        
    def speed_dir(self,event):
        self.speed=[0,0]
        press_key=pygame.key.get_pressed()
        if press_key[K_a]: 
            self.speed[0] = 1
        elif press_key[K_d]: 
            self.speed[0] = -1
        if press_key[K_w]: 
            self.speed[1]= 1
        elif press_key[K_s]: 
            self.speed[1] = -1
        return self.speed
        

    def drawplayer(self,screen):
        torch_image=pygame.image.load("picture/torch.png").convert_alpha()
        woodsword_image=pygame.image.load("picture/woodsword.png").convert_alpha()
        stonesword_image=pygame.image.load("picture/stonesword.png").convert_alpha()
        #picture from game "Don't Starve"
        if self.speed[0]==-1:
            self.walkcount+=1
            if self.walkcount>=0 and self.walkcount<=10 and self.attack_status!=True:
                screen.blit(self.right,(self.x,self.y))
            elif self.walkcount>10 and self.walkcount<=20 and self.attack_status!=True:
                screen.blit(self.rightwalk1,(self.x,self.y))
            elif self.walkcount>20 and self.attack_status!=True:
                screen.blit(self.right,(self.x,self.y))
                self.walkcount=1
            elif self.attack_status==True:
                screen.blit(self.rightattack,(self.x,self.y))
            if self.equip_fire==True:
                screen.blit(torch_image,(298,178))
            elif self.equip_woodsword==True:
                screen.blit(woodsword_image,(300,185))
            elif self.equip_stonesword==True:
                screen.blit(stonesword_image,(300,185))
        elif self.speed[0]==1:
            self.walkcount+=1
            if self.walkcount>=0 and self.walkcount<=10 and self.attack_status!=True:
                screen.blit(self.left,(self.x,self.y))
            elif self.walkcount>10 and self.walkcount<=20 and self.attack_status!=True:
                screen.blit(self.leftwalk1,(self.x,self.y))
            elif self.walkcount>20 and self.attack_status!=True:
                screen.blit(self.left,(self.x,self.y))
                self.walkcount=1
            elif self.attack_status==True:
                screen.blit(self.leftattack,(self.x,self.y))
            if self.equip_fire==True:
                screen.blit(torch_image,(307,174))
            elif self.equip_woodsword==True:
                screen.blit(woodsword_image,(314,185))
            elif self.equip_stonesword==True:
                screen.blit(stonesword_image,(312,183))
        elif self.speed[1]==1:
            self.walkcount+=1
            if self.walkcount>=0 and self.walkcount<=10 and self.attack_status!=True:
                screen.blit(self.backwalk1,(self.x,self.y))
            elif self.walkcount>10 and self.walkcount<=20 and self.attack_status!=True:
                screen.blit(self.backwalk2,(self.x,self.y))
            elif self.walkcount>20 and self.attack_status!=True:
                screen.blit(self.backwalk1,(self.x,self.y))
                self.walkcount=1
            elif self.attack_status==True:
                screen.blit(self.backattack,(self.x,self.y))
            if self.equip_fire==True:
                screen.blit(torch_image,(293,174))
            elif self.equip_woodsword==True:
                screen.blit(woodsword_image,(298,185))
            elif self.equip_stonesword==True:
                screen.blit(stonesword_image,(297,183))
        elif self.speed[1]==-1:
            self.walkcount+=1
            if self.walkcount>=0 and self.walkcount<=10 and self.attack_status!=True:
                screen.blit(self.walk1,(self.x,self.y))
            elif self.walkcount>10 and self.walkcount<=20 and self.attack_status!=True:
                screen.blit(self.walk2,(self.x,self.y))
            elif self.walkcount>20 and self.attack_status!=True:
                screen.blit(self.walk1,(self.x,self.y))
                self.walkcount=1
            elif self.attack_status==True:
                screen.blit(self.frontattack,(self.x,self.y))
            if self.equip_fire==True:
                screen.blit(torch_image,(293,174))
            elif self.equip_woodsword==True:
                screen.blit(woodsword_image,(298,185))
            elif self.equip_stonesword==True:
                screen.blit(stonesword_image,(297,183))
        else:
            if self.attack_status==True:
                screen.blit(self.frontattack,(self.x,self.y))
            else:
                screen.blit(self.front,(self.x,self.y))
            if self.equip_fire==True:
                screen.blit(torch_image,(293,174))
            elif self.equip_woodsword==True:
                screen.blit(woodsword_image,(298,185))
            elif self.equip_stonesword==True:
                screen.blit(stonesword_image,(297,183))
        

            
    def pickup(self,event,item):
        press_key=pygame.key.get_pressed()
        press_mouse=pygame.mouse.get_pressed()
        if item.collided(self) and item.disappear!=True:
            if event.type==MOUSEBUTTONDOWN and press_mouse[0]:
                self.attack_status=True
            elif event.type==MOUSEBUTTONUP:
                if self.attack_status==True:
                    item.health-=self.attack
                    self.attack_status=False
            if press_key[K_SPACE] and item.health<=0 and item.disappear!=True:
                self.event_pickup=True
                if type(item) in self.bag:
                    self.bag[type(item)]+=item.contain
                    item.contain=0
                else:
                    self.bag[type(item)]=item.contain
                    item.contain=0
                    if None in self.bag_list:
                        None_pos=self.bag_list.index(None)
                        self.bag_list[None_pos]=type(item)
                    else:
                        self.bag_list.append(type(item))
                item.disappear=True

    def pickberry(self,event,item):
        press_key=pygame.key.get_pressed()
        if item.collided(self):
            if press_key[K_SPACE] and item.disappear!=True:
                self.event_pickup=True
                if type(item) in self.bag:
                    self.bag[type(item)]+=item.contain
                    item.contain=0
                else:
                    self.bag[type(item)]=item.contain
                    item.contain=0
                    if None in self.bag_list:
                        None_pos=self.bag_list.index(None)
                        self.bag_list[None_pos]=type(item)
                    else:
                        self.bag_list.append(type(item))
                item.disappear=True

    def attack_slime(self,event,slime):
        press_key=pygame.key.get_pressed()
        press_mouse=pygame.mouse.get_pressed()
        if (slime.x>self.x-20 and slime.x<self.x+50 and
            slime.y>self.y-70 and slime.y<self.y+100 and slime.disappear==False):
            if event.type==MOUSEBUTTONDOWN and press_mouse[0]:
                self.attack_status=True
            elif event.type==MOUSEBUTTONUP:
                if self.attack_status==True:
                    slime.health-=self.attack
                    self.attack_status=False
            if slime.health<=0:
                slime.defeated=True
                if press_key[K_SPACE] and slime.disappear!=True:
                    self.event_pickup=True
                    if type(slime) in self.bag:
                        self.bag[type(slime)]+=slime.contain_meat
                        slime.contain_meat=0
                    else:
                        self.bag[type(slime)]=slime.contain_meat
                        slime.contain_meat=0
                        if None in self.bag_list:
                            None_pos=self.bag_list.index(None)
                            self.bag_list[None_pos]=type(slime)
                        else:
                            self.bag_list.append(type(slime))
                    slime.disappear=True
                    
    def eat(self,event,item_type):
        press_mouse=pygame.mouse.get_pressed()
        if item_type in self.bag:
            food_pos=self.bag_list.index(item_type)
            if self.bag[item_type]>0:
                x_range=(35+30*food_pos,35+30*(food_pos+1))
                y_range=(440,470)
                mouse_pos=pygame.mouse.get_pos()
                if (x_range[0]<mouse_pos[0] and x_range[1]>mouse_pos[0] and
                    y_range[0]<mouse_pos[1] and y_range[1]>mouse_pos[1]):
                    if event.type==MOUSEBUTTONDOWN and press_mouse[2]:
                       self.eating=True
                    elif event.type==MOUSEBUTTONUP:
                        if self.eating==True:
                            self.bag[item_type]-=1
                            if item_type==treeclass.berry_tree:
                                self.health+=15
                                self.hunger+=20
                                self.spirit+=5
                            elif item_type==slimeclass.slime:
                                self.health+=5
                                self.hunger+=30
                                self.spirit-=5
                            elif item_type=="meat bowl":
                                self.health+=50
                                self.hunger+=80
                                self.spirit+=20
                            self.eating=False
                            if self.health >100:
                                self.health=100
                            if self.hunger>100:
                                self.hunger=101
                            if self.spirit>100:
                                self.spirit=100
            else:
                del self.bag[item_type]
                self.bag_list[food_pos]=None
                        
        

    def drawpack(self,screen):
        pygame.draw.rect(screen,[209,197,201],[30,440,600,30],0)
        my_font=pygame.font.Font('arial.ttf',10)
        for i in range(20):
            pygame.draw.rect(screen,[0,0,0],[30+30*i,440,30,30],3)
        for item_type in self.bag:
            if self.bag[item_type]>0:
                item_order=self.bag_list.index(item_type)
                text=my_font.render("x%d"%self.bag[item_type],True,(0,0,0))
                screen.blit(text,(40+30*item_order,440))
                if item_type == treeclass.tree:
                    wood_image=pygame.image.load("picture/wood_bag.png").convert_alpha()
                    #picture from game "Don't Starve"
                    screen.blit(wood_image,(30+30*item_order,450))
                elif item_type == slimeclass.slime:
                    meat_image=pygame.image.load("picture/meat_bag.png").convert_alpha()
                    #picture from game "Don't Starve"
                    screen.blit(meat_image,(30+30*item_order,450))
                elif item_type == treeclass.grass:
                    cutgrass_image=pygame.image.load("picture/cutgrass_bag.png").convert_alpha()
                    #picture from game "Don't Starve"
                    screen.blit(cutgrass_image,(30+30*item_order,450))
                elif item_type == treeclass.berry_tree:
                    berry_image=pygame.image.load("picture/berry.png").convert_alpha()
                    #picture from game "Don't Starve"
                    screen.blit(berry_image,(25+30*item_order,450))
                elif item_type ==treeclass.stone:
                    stonecut_image=pygame.image.load("picture/stone_cut_bag.png").convert_alpha()
                    #picture from game "Don't Starve"
                    screen.blit(stonecut_image,(30+30*item_order,448))
                elif item_type =="meat bowl":
                    meat_bowl_image=pygame.image.load("picture/meat_bowl.png").convert_alpha()
                    #picture from game "Don't Starve"
                    screen.blit(meat_bowl_image,(30+30*item_order,447))
            
                

    def attribute_change(self,time_passed_seconds):
        self.hunger-=time_passed_seconds/5
        if self.spirit<100:
            self.spirit+=time_passed_seconds/15
        if self.event_pickup==True:
            self.hunger-=2
            self.event_pickup=False
        if self.being_attacked==True:
            self.spirit-=3
        if self.hunger<100:
            self.health-=time_passed_seconds/5
            self.spirit-=time_passed_seconds/5
        if self.equip_woodsword==True:
            self.attack=15
        if self.equip_stonesword==True:
            self.attack=20
        if self.equip_fire==True and self.spirit<100:
            self.spirit+=time_passed_seconds/5

    def drawattributes(self,screen):
        my_font=pygame.font.Font('arial.ttf',12)
        text_health=my_font.render("HP:%d/100"%self.health,True,(0,0,0))
        pygame.draw.rect(screen,[0,0,0],[540,100,80,20],2)
        pygame.draw.rect(screen,[255,0,0],[541,101,79*self.health/100,19],0)
        screen.blit(text_health,(545,105))
        text_hunger=my_font.render("Hg:%d/100"%self.hunger,True,(0,0,0))
        pygame.draw.rect(screen,[0,0,0],[540,130,80,20],2)
        pygame.draw.rect(screen,[255,165,0],[541,131,79*self.hunger/100,19],0)
        screen.blit(text_hunger,(545,135))
        text_hunger=my_font.render("Sp:%d/100"%self.spirit,True,(0,0,0))
        pygame.draw.rect(screen,[0,0,0],[540,160,80,20],2)
        pygame.draw.rect(screen,[84,255,159],[541,161,79*self.spirit/100,19],0)
        screen.blit(text_hunger,(545,165))

    def draw_equipmentbag(self,screen):
        pygame.draw.rect(screen,[209,197,201],[580,200,40,160],0)
        for i in range(4):
            pygame.draw.rect(screen,[0,0,0],[580,200+40*i,40,40],2)
        if self.equip_bag[0]=="torch":
            torch_image=pygame.image.load("picture/torch_craft.png").convert_alpha()
            #picture from game "Don't Starve"
            screen.blit(torch_image,(590,200))
        if self.equip_bag[1]=="woodsword":
            woodsword_image=pygame.image.load("picture/woodsword_craft.png").convert_alpha()
            #picture from game "Don't Starve"
            screen.blit(woodsword_image,(590,240))
        if self.equip_bag[1]=="stonesword":
            stonesword_image=pygame.image.load("picture/stonesword_craft.png").convert_alpha()
            #picture from game "Don't Starve"
            screen.blit(stonesword_image,(590,240))
        if self.equip_bag[2]=="pot":
            pot_image=pygame.image.load("picture/pot_craft.png").convert_alpha()
            #picture from game "Don't Starve"
            screen.blit(pot_image,(580,285))
        if self.equip_bag[3]=="hat":
            hat_image=pygame.image.load("picture/hat_craft.png").convert_alpha()
            #picture from game "Don't Starve"
            screen.blit(hat_image,(580,325))
            self.front=pygame.image.load("picture/frontman.png").convert_alpha()
            self.right=pygame.image.load("picture/right.png").convert_alpha()
            self.left=pygame.image.load("picture/left.png").convert_alpha()
            self.back=pygame.image.load("picture/back.png").convert_alpha()
            self.walk1=pygame.image.load("picture/frontman_walk.png").convert_alpha()
            self.walk2=pygame.image.load("picture/frontman_walk2.png").convert_alpha()
            self.backwalk1=pygame.image.load("picture/back_walk.png").convert_alpha()
            self.backwalk2=pygame.image.load("picture/back_walk2.png").convert_alpha()
            self.leftwalk1=pygame.image.load("picture/left_walk.png").convert_alpha()
            self.rightwalk1=pygame.image.load("picture/right_walk.png").convert_alpha()
            self.frontattack=pygame.image.load("picture/frontman_attack.png").convert_alpha()
            self.leftattack=pygame.image.load("picture/left_attack.png").convert_alpha()
            self.rightattack=pygame.image.load("picture/right_attack.png").convert_alpha()
            self.backattack=pygame.image.load("picture/back_attack.png").convert_alpha()
            #pictures are from game "Don't Starve"

    def equip(self,event):
        press_mouse=pygame.mouse.get_pressed()
        mouse_pos=pygame.mouse.get_pos()
        press_key=pygame.key.get_pressed()
        if (580<mouse_pos[0] and 620>mouse_pos[0] and
            200<mouse_pos[1] and 240>mouse_pos[1]):
            if (event.type==MOUSEBUTTONDOWN and press_mouse[2] and
                self.equip_bag[0]=="torch"):
                self.equip_fire=True
                self.equip_woodsword=False
                self.equip_stonesword=False
        elif (self.equip_bag[0]=="torch" and  press_key[K_q]):
            self.equip_fire=True
            self.equip_woodsword=False
            self.equip_stonesword=False
        elif (580<mouse_pos[0] and 620>mouse_pos[0] and
            240<mouse_pos[1] and 280>mouse_pos[1]):
            if (event.type==MOUSEBUTTONDOWN and press_mouse[2] and
                self.equip_bag[1]=="woodsword"):
                self.equip_woodsword=True
                self.equip_fire=False
                self.equip_stonesword=False
            elif (event.type==MOUSEBUTTONDOWN and press_mouse[2] and
                  self.equip_bag[1]=="stonesword"):
                self.equip_stonesword=True
                self.equip_fire=False
                self.equip_woodsword=False
        elif (self.equip_bag[1]=="woodsword" and  press_key[K_e]):
            self.equip_woodsword=True
            self.equip_fire=False
            self.equip_stonesword=False
        elif  (self.equip_bag[1]=="stonesword" and  press_key[K_e]):
            self.equip_stonesword=True
            self.equip_fire=False
            self.equip_woodsword=False
        elif (580<mouse_pos[0] and 620>mouse_pos[0] and
            280<mouse_pos[1] and 320>mouse_pos[1]):
            if (event.type==MOUSEBUTTONDOWN and press_mouse[2] and
                self.equip_bag[2]=="pot" and self.open_pot==False):
                self.open_pot=True
            elif (event.type==MOUSEBUTTONDOWN and press_mouse[2] and
                  self.open_pot==True):
                self.open_pot=False

    def cook(self,screen):
        mouse_image=pygame.image.load("picture/meat_bag.png").convert_alpha()
        #picture from game "Don't Starve"
        my_font=pygame.font.Font('arial.ttf',12)
        text=my_font.render("cook",True,(0,0,0))
        if self.open_pot==True:
            pygame.draw.rect(screen,[209,197,201],[540,280,30,135],0)
            pygame.draw.rect(screen,[0,0,0],[540,400,30,15],2)
            screen.blit(text,(542,400))
            for i in range(4):
                pygame.draw.rect(screen,[0,0,0],[540,280+30*i,30,30],2)
                if self.pot_contain[i]!=None:
                    screen.blit(mouse_image,(540,285+30*i))
        if self.food_inmouse==True:
            x,y=pygame.mouse.get_pos()
            x-=mouse_image.get_width()/2
            y-=mouse_image.get_height()/2
            screen.blit(mouse_image,(x,y))
            

    def dragfood(self,event,item_type):
        press_mouse=pygame.mouse.get_pressed()
        mouse_pos=pygame.mouse.get_pos()
        if item_type in self.bag and self.open_pot==True:
            food_pos=self.bag_list.index(item_type)
            if self.bag[item_type]>0:
                x_range=(35+30*food_pos,35+30*(food_pos+1))
                y_range=(440,470)
                if (x_range[0]<mouse_pos[0] and x_range[1]>mouse_pos[0] and
                    y_range[0]<mouse_pos[1] and y_range[1]>mouse_pos[1]):
                    if event.type==MOUSEBUTTONDOWN and press_mouse[0] and self.drag_food==False:
                        self.drag_food=True
                    elif event.type==MOUSEBUTTONUP:
                        self.food_inmouse=True
                        if self.drag_food==True:
                            self.bag[item_type]-=1
                            self.drag_food=False
            else:
                del self.bag[item_type]
                self.bag_list[food_pos]=None
                                

    def placefood(self,event,item_type):
        press_mouse=pygame.mouse.get_pressed()
        mouse_pos=pygame.mouse.get_pos()
        if self.food_inmouse==True:
            for i in range(4):
                x_range=(540,570)
                y_range=(280+30*i,280+30*(i+1))
                if (x_range[0]<mouse_pos[0] and x_range[1]>mouse_pos[0] and
                    y_range[0]<mouse_pos[1] and y_range[1]>mouse_pos[1]):
                    if (event.type==MOUSEBUTTONDOWN and press_mouse[0]
                        and self.pot_contain[i]==None):
                        self.food_inmouse=False
                        self.pot_contain[i]="meat"
                        
        
    def clickcook(self,event):
        press_mouse=pygame.mouse.get_pressed()
        mouse_pos=pygame.mouse.get_pos()
        if (540<mouse_pos[0] and 570>mouse_pos[0] and 400<mouse_pos[1] and
            415>mouse_pos[1] and self.open_pot==True):
            n=0
            for i in self.pot_contain:
                if i =="meat":
                    n+=1
            if (event.type==MOUSEBUTTONDOWN and press_mouse[0] and n>2):
                self.pot_contain=[None]*4
                if "meat bowl" in self.bag:
                    self.bag["meat bowl"]+=1
                else:
                    self.bag["meat bowl"]=1
                    if None in self.bag_list:
                        None_pos=self.bag_list.index(None)
                        self.bag_list[None_pos]="meat bowl"
                    else:
                        self.bag_list.append("meat bowl")
                
            
        
            

    def craft_menu(self,screen):
        pygame.draw.rect(screen,[209,197,201],[20,100,40,200],0)
        wood_image=pygame.image.load("picture/wood.png").convert_alpha()
        cutgrass_image=pygame.image.load("picture/cutgrass.png").convert_alpha()
        stone_image=pygame.image.load("picture/stone_cut.png").convert_alpha()
        #picture from game "Don't Starve"
        my_font=pygame.font.Font('arial.ttf',15)
        text1=my_font.render("x1",True,(0,0,0))
        text2=my_font.render("x2",True,(0,0,0))
        text5=my_font.render("x5",True,(0,0,0))
        text10=my_font.render("x10",True,(0,0,0))
        torch_image=pygame.image.load("picture/torch_craft.png").convert_alpha()
        stonesword_image=pygame.image.load("picture/stonesword_craft.png").convert_alpha()
        woodsword_image=pygame.image.load("picture/woodsword_craft.png").convert_alpha()
        pot_image=pygame.image.load("picture/pot_craft.png").convert_alpha()
        hat_image=pygame.image.load("picture/hat_craft.png").convert_alpha()
        #picture from game "Don't Starve"
        screen.blit(torch_image,(30,100))
        screen.blit(woodsword_image,(30,140))
        screen.blit(stonesword_image,(30,180))
        screen.blit(pot_image,(20,225))
        screen.blit(hat_image,(20,265))
        for i in range(5):
            pygame.draw.rect(screen,[0,0,0],[20,100+40*i,40,40],2)
            if self.open_craft[i]==True:
                if i==0:
                    pygame.draw.rect(screen,[209,197,201],[60,100,105,40],0)
                    pygame.draw.rect(screen,[0,0,0],[60,100,105,40],2)
                    screen.blit(wood_image,(60,105))
                    screen.blit(cutgrass_image,(105,105))
                    screen.blit(text2,(100,110))
                    screen.blit(text2,(145,110))
                elif i==1:
                    pygame.draw.rect(screen,[209,197,201],[60,140,105,40],0)
                    pygame.draw.rect(screen,[0,0,0],[60,140,105,40],2)
                    screen.blit(wood_image,(60,145))
                    screen.blit(stone_image,(105,145))
                    screen.blit(text5,(100,150))
                    screen.blit(text2,(145,150))
                elif i==2:
                    pygame.draw.rect(screen,[209,197,201],[60,180,105,40],0)
                    pygame.draw.rect(screen,[0,0,0],[60,180,105,40],2)
                    screen.blit(wood_image,(60,185))
                    screen.blit(stone_image,(105,185))
                    screen.blit(text2,(100,190))
                    screen.blit(text5,(145,190))
                elif i==3:
                    pygame.draw.rect(screen,[209,197,201],[60,220,155,40],0)
                    pygame.draw.rect(screen,[0,0,0],[60,220,155,40],2)
                    screen.blit(stone_image,(52,225))
                    screen.blit(wood_image,(108,225))
                    screen.blit(cutgrass_image,(152,225))
                    screen.blit(text10,(90,230))
                    screen.blit(text2,(150,230))
                    screen.blit(text2,(197,230))
                elif i==4:
                    pygame.draw.rect(screen,[209,197,201],[60,260,60,40],0)
                    pygame.draw.rect(screen,[0,0,0],[60,260,60,40],2)
                    screen.blit(cutgrass_image,(55,265))
                    screen.blit(text10,(95,270))
                    
    def deleteitem(self,item):
        if item in self.bag and self.bag[item]<=0:
            item_order=self.bag_list.index(item)
            del self.bag[item]
            self.bag_list[item_order]=None
            

    def craft(self,event):
        press_mouse=pygame.mouse.get_pressed()
        mouse_pos=pygame.mouse.get_pos()
        for i in range(5):
            if (20<mouse_pos[0] and 60>mouse_pos[0] and
                100+40*i<mouse_pos[1] and 140+40*i>mouse_pos[1]):
                if (event.type==MOUSEBUTTONDOWN and press_mouse[0] and
                    self.open_craft[i]==False):
                    self.open_craft[i]=True
                elif (event.type==MOUSEBUTTONDOWN and press_mouse[0] and
                      self.open_craft[i]==True):
                    self.open_craft[i]=False
        if (60<mouse_pos[0] and 165>mouse_pos[0] and
            100<mouse_pos[1] and 140>mouse_pos[1] and self.open_craft[0]==True):
            if (event.type==MOUSEBUTTONDOWN and press_mouse[0]):
                if (self.bag[treeclass.tree]>=2 and self.bag[treeclass.grass]>=2):
                    self.bag[treeclass.tree]-=2
                    self.bag[treeclass.grass]-=2
                    if self.equip_bag[0]==None:
                        self.equip_bag[0]="torch"
        elif(60<mouse_pos[0] and 165>mouse_pos[0] and
            140<mouse_pos[1] and 180>mouse_pos[1] and self.open_craft[1]==True):
            if (event.type==MOUSEBUTTONDOWN and press_mouse[0]):
                if (self.bag[treeclass.tree]>=5 and self.bag[treeclass.stone]>=2):
                    self.bag[treeclass.tree]-=5
                    self.bag[treeclass.stone]-=2
                    if self.equip_bag[1]!="woodsword":
                        self.equip_bag[1]="woodsword"
        elif(60<mouse_pos[0] and 165>mouse_pos[0] and
            180<mouse_pos[1] and 220>mouse_pos[1] and self.open_craft[2]==True):
            if (event.type==MOUSEBUTTONDOWN and press_mouse[0]):
                if (self.bag[treeclass.tree]>=2 and self.bag[treeclass.stone]>=5):
                    self.bag[treeclass.tree]-=2
                    self.bag[treeclass.stone]-=5
                    if self.equip_bag[1]!="stonesword":
                        self.equip_bag[1]="stonesword"
        elif(60<mouse_pos[0] and 215>mouse_pos[0] and
            220<mouse_pos[1] and 260>mouse_pos[1] and self.open_craft[3]==True):
            if (event.type==MOUSEBUTTONDOWN and press_mouse[0]):
                if (self.bag[treeclass.stone]>=10 and self.bag[treeclass.tree]>=2
                    and self.bag[treeclass.grass]>=2):
                    self.bag[treeclass.stone]-=10
                    self.bag[treeclass.tree]-=2
                    self.bag[treeclass.grass]-=2
                    if self.equip_bag[2]==None:
                        self.equip_bag[2]="pot"
        elif(60<mouse_pos[0] and 120>mouse_pos[0] and
            260<mouse_pos[1] and 300>mouse_pos[1] and self.open_craft[4]==True):
            if (event.type==MOUSEBUTTONDOWN and press_mouse[0]):
                if (self.bag[treeclass.grass]>=10):
                    self.bag[treeclass.grass]-=10
                    if self.equip_bag[3]==None:
                        self.equip_bag[3]="hat"
        self.deleteitem(treeclass.stone)
        self.deleteitem(treeclass.grass)
        self.deleteitem(treeclass.tree)

    def basic_teleport(self,wormhole):
        press_key=pygame.key.get_pressed()
        if wormhole.collided(self) and press_key[K_SPACE]:
            self.teleport_status=True
            return True

    def discovermap(self):
        if self.originalx/10+330>self.maxx:
            self.maxx=self.originalx/10+330
        if self.originalx/10+330<self.leastx:
            self.leastx=self.originalx/10+330
        if self.originaly/10+220>self.maxy:
            self.maxy=self.originaly/10+220
        if self.originaly/10+220<self.leasty:
            self.leasty=self.originaly/10+220
            
           



        
