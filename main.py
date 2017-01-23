import pygame
from pygame.locals import *
import random
import playerclass
import treeclass
import slimeclass
import time

def splashscreen():
    pygame.init()
    screen=pygame.display.set_mode((640, 480),0,32)
    bg=pygame.image.load("picture/splash_screen_word.jpg").convert()
    #picture from game "Don't Starve"
    rulespic=pygame.image.load("picture/rules.jpg").convert()
    pygame.display.set_caption("Isolation")
    start_pos=[450,340,580,380]
    load_pos=[450,390,580,420]
    rules_pos=[450,430,580,460]
    gameexit=False
    displayscore=False
    load=False
    rulesdisplay=False
    daycount=1
    pygame.mixer.music.load("song/Main.ogg")
    #music from game "Don't Starve"
    pygame.mixer.music.play(-1,0)
    while not gameexit:
        screen.blit(bg,[0,0])
        event=pygame.event.poll()
        press_mouse=pygame.mouse.get_pressed()
        mouse_pos=pygame.mouse.get_pos()
        if displayscore==True:
            draw_displayscore(daycount,screen)
        if (event.type==MOUSEBUTTONDOWN and press_mouse[0]):
            if (start_pos[0]<mouse_pos[0] and start_pos[2]>mouse_pos[0]
                and start_pos[1]<mouse_pos[1] and start_pos[3]>mouse_pos[1]):
                if main_run(daycount,load)==False:
                    displayscore=True
            elif (load_pos[0]<mouse_pos[0] and load_pos[2]>mouse_pos[0]
                and load_pos[1]<mouse_pos[1] and load_pos[3]>mouse_pos[1]):
                load=True
                if main_run(daycount,load)==False:
                    displayscore=True
            elif (rules_pos[0]<mouse_pos[0] and rules_pos[2]>mouse_pos[0]
                and rules_pos[1]<mouse_pos[1] and rules_pos[3]>mouse_pos[1]):
                rulesdisplay=True
            elif (260<mouse_pos[0] and 346>mouse_pos[0]
                and 353<mouse_pos[1] and 393>mouse_pos[1] and rulesdisplay==True):
                rulesdisplay=False
        if rulesdisplay==True:
            screen.blit(rulespic,[0,0])
        if event.type==pygame.QUIT:
            gameexit=True
        pygame.display.update()
    pygame.quit()
    

def draw_displayscore(daycount,screen):
    my_font=pygame.font.Font('arial.ttf',25)
    text=my_font.render("Survival days:%d"%daycount,True,(255,255,255))
    screen.blit(text,[120,350])

    
def islegal_map(pos):
    if pos[0]>2200:
        pos[0]=2200
    if pos[0]<-1680:
        pos[0]=-1680
    if pos[1]>1200:
        pos[1]=1200
    if pos[1]<-720:
        pos[1]=-720
    return pos

def islegal_dir(pos,speed_dir):
    if pos[0]>=2200 or  pos[0]<=-1680:
       speed_dir[0]=0
    if pos[1]>=1200 or pos[1]<=-720:
        speed_dir[1]=0
    return speed_dir

def create_tree():
    tree=[]
    for i in range(20):
        x=random.randint(0,1680)
        y=random.randint(0,720)
        tree.append(treeclass.tree(x,y))
    return tree

def create_grass():
    grass=[]
    for i in range(20):
        x=random.randint(0,1680)
        y=random.randint(-760,0)
        grass.append(treeclass.grass(x,y))
    return grass

def create_berry_tree():
    berry_tree=[]
    for i in range(20):
        x=random.randint(-1680,0)
        y=random.randint(-760,0)
        berry_tree.append(treeclass.berry_tree(x,y))
    return berry_tree

def create_slime():
    slime=[]
    for i in range(15):
        x=int(random.randint(-1680,1680))
        y=int(random.randint(-760,760))
        slime.append(slimeclass.slime(x,y))
    return slime

def create_stone():
    stone=[]
    for i in range(20):
        x=random.randint(-1680,0)
        y=random.randint(0,760)
        stone.append(treeclass.stone(x,y))
    return stone 

def create_wormhole():
    wormhole1=treeclass.wormhole(-200,-300)
    wormhole2=treeclass.wormhole(300,400)
    wormhole=[wormhole1,wormhole2]
    return wormhole

    
def draw_smallmap(screen):
    small_map=screen.copy()
    small_map=pygame.transform.scale(small_map,(96,72))
    screen.blit(small_map,[531,21])
    pygame.draw.rect(screen,[0,0,0],[530,20,96,72],2)

def change_environment(screen,i,player):
    if i>=38 and i<58:
        pic=pygame.image.load("picture/afternoon.jpg")
        #picture from game "Don't Starve"
        pic.set_alpha(220)
        screen.blit(pic,(0,0))
        if player.equip_fire==True:
            pic2=pygame.image.load("picture/afternoon_1.jpg")
            #picture from game "Don't Starve"
            pic2.set_alpha(100)
            screen.blit(pic2,(0,0))
    elif i>=58:
        pic=pygame.image.load("picture/evening.jpg")
        #picture from game "Don't Starve"
        pic.set_alpha(220)
        screen.blit(pic,(0,0))
        if player.equip_fire==True:
            pic2=pygame.image.load("picture/evening_1.jpg")
            #picture from game "Don't Starve"
            pic2.set_alpha(150)
            screen.blit(pic2,(0,0))

def drawtimepass(screen,i,daycount):    
    pygame.draw.rect(screen,[0,0,0],[280,20,80,30],2)
    pygame.draw.rect(screen,[245,221,98],[282,22,38,27],0)
    pygame.draw.rect(screen,[133,28,67],[320,22,20,27],0)
    pygame.draw.rect(screen,[32,38,51],[340,22,20,27],0)
    pygame.draw.line(screen,[0,0,0],(280+i,20),(280+i,50),2)
    my_font=pygame.font.Font('arial.ttf',20)
    text=my_font.render("Day:%d"%daycount,True,(0,0,0))
    screen.blit(text,(220,20))

def draw_bigmap(screen,tree,slime,player,grass,berry_tree,stone,wormhole):
    bigmap=pygame.image.load("picture/bigmap.jpg")
    treeimage=pygame.image.load("picture/treemap.png")
    stoneimage=pygame.image.load("picture/stonemap.png")
    grassimage=pygame.image.load("picture/grassmap.png")
    slimeimage=pygame.image.load("picture/spidermap.png")
    playerimage=pygame.image.load("picture/playermap.png")
    wormholeimage=pygame.image.load("picture/wormholemap.png")
    berrytreeimage=pygame.image.load("picture/berrytreemap.png")
    #picture are all from game "Don't Starve"
    press_key=pygame.key.get_pressed()
    if press_key[K_TAB]:
        screen.blit(bigmap,(80,100))
        pygame.draw.rect(screen,[0,0,0],[80,100,500,240],1)
        for t in tree:
            screen.blit(treeimage,(t.originalx/10+330,t.originaly/10+220))
        for st in stone:
            screen.blit(stoneimage,(st.originalx/10+330,st.originaly/10+220))
        for b in berry_tree:
            screen.blit(berrytreeimage,(b.originalx/10+330,b.originaly/10+220))
        for g in grass:
            screen.blit(grassimage,(g.originalx/10+330,g.originaly/10+220))
        for w in wormhole:
            screen.blit(wormholeimage,(w.originalx/10+330,w.originaly/10+220))
        for s in slime:
            screen.blit(slimeimage,(s.originalx/10+330,s.originaly/10+220))
        playerx=player.originalx/10+330
        playery=player.originaly/10+220
        screen.blit(playerimage,(playerx,playery))
        player.discovermap()
        pygame.draw.rect(screen,[0,0,0],[80,100,player.leastx-80-10,240],0)
        pygame.draw.rect(screen,[0,0,0],[player.leastx-10,100,
                                         580-player.leastx+10,player.leasty-100-10],0)
        pygame.draw.rect(screen,[0,0,0],[player.maxx+20,player.leasty-10,
                                         580-player.maxx-20,340-player.leasty+10],0)   
        pygame.draw.rect(screen,[0,0,0],[player.leastx-10,player.maxy+30,
                                         player.maxx-player.leastx+30+1,340-player.maxy-30],0)

def teleport(player,wormhole,current_pos,tree,slime,grass,berry_tree,stone):
    for i in wormhole:
        if player.basic_teleport(i)==True:
            if i==wormhole[1]:
                x=480
                y=650
                current_pos[0]+=x
                current_pos[1]+=y
                for t in tree:
                    t.x+=x
                    t.y+=y
                for g in grass:
                    g.x+=x
                    g.y+=y
                for b in berry_tree:
                    b.x+=x
                    b.y+=y
                for st in stone:
                    st.x+=x
                    st.y+=y
                for s in slime:
                    s.x+=x
                    s.y+=y
                for w in wormhole:
                    w.x+=x
                    w.y+=y
                player.originalx-=x
                player.originaly-=y
            elif i==wormhole[0]:
                x=520
                y=750
                current_pos[0]-=x
                current_pos[1]-=y
                for t in tree:
                    t.x-=x
                    t.y-=y
                for g in grass:
                    g.x-=x
                    g.y-=y
                for b in berry_tree:
                    b.x-=x
                    b.y-=y
                for st in stone:
                    st.x-=x
                    st.y-=y
                for s in slime:
                    s.x-=x
                    s.y-=y
                for w in wormhole:
                    w.x-=x
                    w.y-=y
                player.originalx+=x
                player.originaly+=y

def drawpause(screen):
    pausescreen=pygame.image.load("picture/pause.jpg")
    #picture from game "Don't Starve"
    screen.blit(pausescreen,(0,0))

def pause_Exit(event):
    press_mouse=pygame.mouse.get_pressed()
    mouse_pos=pygame.mouse.get_pos()
    if (mouse_pos[0]>336 and mouse_pos[0]<336+74 and
        mouse_pos[1]>310 and mouse_pos[1]<310+36 and
        event.type==MOUSEBUTTONDOWN and press_mouse[0]):
        return True

def pause_save(event,player,tree,grass,berry_tree,stone,slime,wormhole,daycount,current_pos):
    press_mouse=pygame.mouse.get_pressed()
    mouse_pos=pygame.mouse.get_pos()
    if (mouse_pos[0]>234 and mouse_pos[0]<234+74 and
        mouse_pos[1]>310 and mouse_pos[1]<310+36 and
        event.type==MOUSEBUTTONDOWN and press_mouse[0]):
        savefile(player,tree,grass,berry_tree,stone,slime,wormhole,daycount,current_pos)

def savefile(player,tree,grass,berry_tree,stone,slime,wormhole,daycount,current_pos):
    playercontent0=str(round(float(player.originalx)))+","+str(round(float(player.originaly)))
    playercontent1=(str(round(float(player.health)))+","+str(round(float(player.hunger)))+","+
                    str(round(float(player.spirit))))
    playercontent2=""
    for item in player.bag:
        playercontent2+=str(item)+":"+str(player.bag[item])+","
    playercontent3=""
    for item in player.bag_list:
        playercontent3+=str(item)+","
    playercontent4=""
    for item in player.equip_bag:
         playercontent4+=str(item)+","
    playercontent5=(str(round(float(player.maxx)))+","+str(round(float(player.maxy)))+","
                    +str(round(float(player.leastx)))+","+str(round(float(player.leasty))))
    playercontent=(playercontent0+"\n"+playercontent1+"\n"+playercontent2+"\n"+
                  playercontent3+"\n"+playercontent4+"\n"+playercontent5)
    treecontent=""
    for t in tree:
        treecontent+=(str(round(float(t.x)))+","+str(round(float(t.y)))+","+str(t.originalx)+","+
                        str(t.originaly)+","+str(t.disappear)+"\t")
    grasscontent=""
    for g in grass:
        grasscontent+=(str(round(float(g.x)))+","+str(round(float(g.y)))+","+str(g.originalx)+","+
                       str(g.originaly)+","+str(g.disappear)+"\t")
    berry_treecontent=""
    for b in berry_tree:
        berry_treecontent+=(str(round(float(b.x)))+","+str(round(float(b.y)))+","+str(b.originalx)+","+
                            str(b.originaly)+","+str(b.disappear)+"\t")
    stonecontent=""
    for st in stone:
        stonecontent+=(str(round(float(st.x)))+","+str(round(float(st.y)))+","+
                       str(st.originalx)+","+str(st.originaly)+","+str(st.disappear)+"\t")
    wormholecontent=""
    for w in wormhole:
        wormholecontent+=(str(round(float(w.x)))+","+str(round(float(w.y)))+","+
                          str(w.originalx)+","+str(w.originaly)+"\t")
    slimecontent=""
    for s in slime:
        slimecontent+=(str(round(float(s.x)))+","+str(round(float(s.y)))+","+str(s.originalx)+","+
                       str(s.originaly)+","+str(s.defeated)+","+str(s.disappear)+"\t")
    content=(playercontent+"\n"+treecontent+"\n"+grasscontent+"\n"+
             berry_treecontent+"\n"+stonecontent+"\n"+wormholecontent+"\n"+
             slimecontent+"\n"+str(daycount)+"\n"+str(round(float(current_pos[0])))
             +","+str(round(float(current_pos[0]))))
    with open('save/isolation_save.txt',"wt") as f:
        f.write(content)
        
def str2bool(word):
    return (word=="True")

def str2none(word):
    if word=="None":
        return None
    else:
        return str2classtype(word)

def str2classtype(word):
    if word=="<class 'slimeclass.slime'>":
        return slimeclass.slime
    elif word=="<class 'treeclass.tree'>":
        return treeclass.tree
    elif word=="<class 'treeclass.grass'>":
        return treeclass.grass
    elif word=="<class 'treeclass.berry_tree'>":
        return treeclass.berry_tree
    elif word=="<class 'treeclass.stone'>":
        return treeclass.stone
    else:
        return word
    

def loadfile(player,tree,grass,berry_tree,stone,slime,wormhole,daycount,current_pos):
    with open('save/isolation_save.txt',"rt") as f:
        content=f.read()
        content=content.split("\n")
        for i in range(len(content)):
            if i==0:
                playercontent0=content[0].split(",")
                player.originalx,player.originaly=int(playercontent0[0]),int(playercontent0[1])
            elif i==1:
                playercontent1=content[1].split(",")
                player.health=int(playercontent1[0])
                player.hunger=int(playercontent1[1])
                player.spirit=int(playercontent1[2])
            elif i==2:
                playercontent2=content[2].split(",")
                for item in playercontent2:
                    if item!="":
                        colonindex=item.index(":")
                        key=str2classtype(item[:colonindex])
                        player.bag[key]=int(item[colonindex+1:])     
            elif i==3:
                playercontent3=content[3].split(",")
                for item in playercontent3:
                    if item!="":
                        player.bag_list.append(str2none(item))
            elif i==4:
                playercontent4=content[4].split(",")
                for s in range(len(playercontent4)):
                    if playercontent4[s]!="":
                        player.equip_bag[s]=str2none(playercontent4[s])
            elif i==5:
                playercontent5=content[5].split(",")
                player.maxx=int(playercontent5[0])
                player.maxy=int(playercontent5[1])
                player.leastx=int(playercontent5[2])
                player.leasty=int(playercontent5[3])
            elif i==6:
                treecontent=content[6].split("\t")
                for s in range(len(treecontent)):
                    if treecontent[s]!="":
                        tcontent=treecontent[s].split(",")
                        tree[s].x,tree[s].y=int(tcontent[0]),int(tcontent[1])
                        tree[s].originalx,tree[s].originaly=int(tcontent[2]),int(tcontent[3])
                        tree[s].disappear=str2bool(tcontent[4])
            elif i==7:
                grasscontent=content[7].split("\t")
                for s in range(len(grasscontent)):
                    if grasscontent[s]!="":
                        gcontent=grasscontent[s].split(",")
                        grass[s].x,grass[s].y=int(gcontent[0]),int(gcontent[1])
                        grass[s].originalx,grass[s].originaly=int(gcontent[2]),int(gcontent[3])
                        grass[s].disappear=str2bool(gcontent[4])
            elif i==8:
                berry_treecontent=content[8].split("\t")
                for s in range(len(berry_treecontent)):
                    if berry_treecontent[s]!="":
                        bcontent=berry_treecontent[s].split(",")
                        berry_tree[s].x,berry_tree[s].y=int(bcontent[0]),int(bcontent[1])
                        berry_tree[s].originalx,berry_tree[s].originaly=int(bcontent[2]),int(bcontent[3])
                        berry_tree[s].disappear=str2bool(bcontent[4])
            elif i==9:
                stonecontent=content[9].split("\t")
                for s in range(len(stonecontent)):
                    if stonecontent[s]!="":
                        stcontent=stonecontent[s].split(",")
                        stone[s].x,stone[s].y=int(stcontent[0]),int(stcontent[1])
                        stone[s].originalx,stone[s].originaly=int(stcontent[2]),int(stcontent[3])
                        stone[s].disappear=str2bool(stcontent[4])
            elif i==10:
                wormholecontent=content[10].split("\t")
                for s in range(len(wormholecontent)):
                    if wormholecontent[s]!="":
                        wcontent=wormholecontent[s].split(",")
                        wormhole[s].x,wormhole[s].y=int(wcontent[0]),int(wcontent[1])
                        wormhole[s].originalx,wormhole[s].originaly=int(wcontent[2]),int(wcontent[3])
            elif i==11:
                slimecontent=content[11].split("\t")
                for s in range(len(slimecontent)):
                    if slimecontent[s]!="":
                        scontent=slimecontent[s].split(",")
                        slime[s].x,slime[s].y=int(scontent[0]),int(scontent[1])
                        slime[s].originalx,slime[s].originaly=int(scontent[2]),int(scontent[3])
                        slime[s].defeated=str2bool(scontent[4])
                        slime[s].disappear=str2bool(scontent[5])
            elif i==12:
                daycount=int(content[12])
            elif i==13:
                poscontent=content[13].split(",")
                current_pos[0]=int(poscontent[0])
                current_pos[1]=int(poscontent[1])


def timerfired(clock,player,current_pos,current_speed_dir,tree,
               slime,grass,berry_tree,stone,wormhole):
    time_passed=clock.tick(30)
    time_passed_seconds=time_passed/1000
    speed=80
    current_pos[0]+=current_speed_dir[0]*speed*time_passed_seconds
    current_pos[1]+=current_speed_dir[1]*speed*time_passed_seconds
    speed_dir=islegal_dir(current_pos,current_speed_dir)
    for t in tree:
        t.x+=speed_dir[0]*speed*time_passed_seconds
        t.y+=speed_dir[1]*speed*time_passed_seconds
    for g in grass:
        g.x+=speed_dir[0]*speed*time_passed_seconds
        g.y+=speed_dir[1]*speed*time_passed_seconds
    for b in berry_tree:
        b.x+=speed_dir[0]*speed*time_passed_seconds
        b.y+=speed_dir[1]*speed*time_passed_seconds
    for st in stone:
        st.x+=speed_dir[0]*speed*time_passed_seconds
        st.y+=speed_dir[1]*speed*time_passed_seconds
    for s in slime:
        s.x+=speed_dir[0]*speed*time_passed_seconds
        s.y+=speed_dir[1]*speed*time_passed_seconds
        s.slime_attack(player,time_passed_seconds)
    for w in wormhole:
        w.x+=speed_dir[0]*speed*time_passed_seconds
        w.y+=speed_dir[1]*speed*time_passed_seconds
    player.attribute_change(time_passed_seconds)
    player.originalx-=speed_dir[0]*speed*time_passed_seconds
    player.originaly-=speed_dir[1]*speed*time_passed_seconds
    
def redrawall(screen,bg,current_pos,tree,slime,player,grass,berry_tree,stone,
              elapsetime,daycount,wormhole):
    screen.blit(bg,current_pos)
    screen.blit(bg,[current_pos[0]-2500,current_pos[1]])
    screen.blit(bg,[current_pos[0]-2500,current_pos[1]-1200])
    screen.blit(bg,[current_pos[0],current_pos[1]-1200])
    for t in tree:
        t.drawtree(screen)
    for g in grass:
        g.drawgrass(screen)
    for b in berry_tree:
        b.drawberry(screen)
    for st in stone:
        st.drawstone(screen)
    for w in wormhole:
        w.drawwormhole(screen)
    player.drawplayer(screen)
    for s in slime:
        s.drawslime(screen)
    change_environment(screen,elapsetime,player)
    draw_smallmap(screen)
    drawtimepass(screen,elapsetime,daycount)
    player.drawpack(screen)
    player.drawattributes(screen)
    player.craft_menu(screen)
    player.draw_equipmentbag(screen)
    player.cook(screen)
    if player.teleport_status==True:
        player.teleport_count+=1
        pic=pygame.image.load("picture/real_wormhole.jpg")
        #picture from game "Don't Starve"
        screen.blit(pic,(0,0))
        if player.teleport_count==30:
            player.teleport_status=False
            player.teleport_count=1
    
def main_run(daycount,load):
    pygame.mixer.music.stop()
    pygame.init()
    #window_size=(0,0,640,480)
    screen=pygame.display.set_mode((640, 480),0,32)
    bg=pygame.image.load("picture/map.jpg").convert()
    gg=pygame.image.load("picture/isolation_gameover.jpg")
    #picture from game "Don't Starve"
    pygame.display.set_caption("Isolation")
    clock=pygame.time.Clock()
    player=playerclass.player1(300,150)
    current_pos=[0,0]
    tree=create_tree()
    slime=create_slime()
    grass=create_grass()
    stone=create_stone()
    wormhole=create_wormhole()
    berry_tree=create_berry_tree()
    food=[treeclass.berry_tree,slimeclass.slime,"meat bowl"]
    gameover=False
    gameexit=False
    pause=False
    starttime=time.time()
    pygame.mixer.music.load("song/AutumnWorking.ogg")
    #music from game "Don't Starve"
    pygame.mixer.music.play(-1,0)
    if load==True:
        loadfile(player,tree,grass,berry_tree,stone,slime,wormhole,daycount,current_pos)
    while not (gameover or gameexit):
        event=pygame.event.poll()
        if event.type == pygame.QUIT:
            gameover=True
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE and pause==False:
                pause=True
            elif event.key==K_ESCAPE and pause==True:
                pause=False
        if not pause:
            current_speed_dir=player.speed_dir(event)
            current_pos=islegal_map(current_pos)
            for t in tree:
                player.pickup(event,t)
            for g in grass:
                player.pickup(event,g)
            for b in berry_tree:
                player.pickberry(event,b)
            for st in stone:
                player.pickup(event,st)
            for s in slime:
                player.attack_slime(event,s)
            for f in food:
                player.eat(event,f)
            player.craft(event)
            player.dragfood(event,slimeclass.slime)
            player.placefood(event,slimeclass.slime)
            timerfired(clock,player,current_pos,current_speed_dir,
                       tree,slime,grass,berry_tree,stone,wormhole)
            endtime=time.time()
            elapsetime=(endtime-starttime)/2
            if elapsetime>80:
                starttime=endtime
                daycount+=1
            redrawall(screen,bg,current_pos,tree,slime,player,grass,berry_tree,
                      stone,elapsetime,daycount,wormhole)
            player.equip(event)
            player.clickcook(event)
            teleport(player,wormhole,current_pos,tree,slime,grass,berry_tree,stone)
            draw_bigmap(screen,tree,slime,player,grass,berry_tree,stone,wormhole)
            if player.health <1 or player.hunger <1 or player.spirit<1:
                screen.blit(gg,[0,0])
                player.ggcount+=1
                if player.ggcount>=80:
                    gameover=True
        else:
            drawpause(screen)
            gameexit=pause_Exit(event)
            pause_save(event,player,tree,grass,berry_tree,stone,slime,wormhole,daycount,current_pos)
        pygame.display.update()
    return False
    
    
    

if __name__ == '__main__': 
    splashscreen()
