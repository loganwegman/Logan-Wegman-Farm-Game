#import everything needed
import pygame
from background import *
from farmer import Farmer
from random import randint,choice
pygame.init()
pygame.mixer.init()
ticks=pygame.time.Clock()
#constants
TS=16
TS1=17
W=TS*45
H=TS*30
speed=2.5

#lists for obastacles/other things
trees=[]
rocks=[]
lil_trees=[]
sunflowers=[]
grasss=[]
weeds=[]
roots=[]
soils=[]
flower_grounds=[]
fancy_grasss=[]
carrots=[]
plums=[]
corns=[]
#instances for structures
house=House()
well=Well()
market=Market()
#instances for inventory
ax_slot=Ax_slot()
hoe_slot=Hoe_slot()
water_slot=Water_slot()
pickaxe_slot=Pickaxe_slot()
scythe_slot=Scythe_slot()
backpack=Backpack()
#structure rectangles
house_rect=house.rect
well_rect=well.rect
market_rect=market.rect
door_rect=(house_rect.left+TS,house_rect.bottom,TS,TS)
#tilesheet
tile_sheet=pygame.image.load('tilemap.png')
#load screen
screen=pygame.display.set_mode((W,H))
#make bg size of screen
bg=pygame.Surface((W,H))
green=(132,198,105)
#fill bg with green color
bg.fill(green)
#create instances of the classes
house.Barn()
farmer=Farmer(9.4*TS,19.2*TS)
clock=Clock()
inventory=Inventory()
market_UI=Market_UI()
#create a cleared space for the farmer to intially move
clear_rect=pygame.Rect(house_rect.left-TS, house_rect.bottom, house_rect.width + 2*TS, 5*TS)
screen_Rect=pygame.Rect(0,0,W,H)
#create a list of where obstacles are places
filled_rects=[house_rect,clear_rect,well_rect,market_rect]
#list for the ground details
ground_details=[]

#flower ground details
for i in range(50):
    x=randint(1,45)
    y=randint(1,30)
    flower_ground=Flower_ground(x*TS,y*TS)
    if flower_ground.rect.collidelist(ground_details)==-1:
        flower_grounds.append(flower_ground)
        ground_details.append(flower_ground.rect)

#grass ground details
for i in range(50):
    x=randint(1,45)
    y=randint(1,30)
    fancy_grass=Fancy_grass(x*TS,y*TS)
    if fancy_grass.rect.collidelist(ground_details)==-1:
        fancy_grasss.append(fancy_grass)
        ground_details.append(fancy_grass.rect)

#big tree
for i in range(200):
    x=randint(16,W)
    y=randint(16,H)
    tree=Tree(x,y)
    #if obstacle is placed in a new spot with no other obstacles, add it to the list if there is not collision
    #collide list returns an index of -1 in 0 collisions occure
    if tree.rect.collidelist(filled_rects)==-1:
        #add the object to its list and then to the filled_rects so it cannot have another object placed over it
        trees.append(tree)
        filled_rects.append(tree.rect)
#repeat with other objects
#rocks
for i in range(100):
    x=randint(12,W)
    y=randint(12,H)
    rock=Rock(x,y)
    if rock.rect.collidelist(filled_rects)==-1:
        rocks.append(rock)
        filled_rects.append(rock.rect)

#little tree
for i in range(100):
    x=randint(12,W)
    y=randint(12,H)
    lil_tree=Lil_Tree(x,y)
    if lil_tree.rect.collidelist(filled_rects)==-1:
        lil_trees.append(lil_tree)
        filled_rects.append(lil_tree.rect)
   
#sunflower
for i in range(50):
    x=randint(12,W)
    y=randint(12,H)
    sunflower=Sunflower(x,y)
    if sunflower.rect.collidelist(filled_rects)==-1:
        sunflowers.append(sunflower)
        filled_rects.append(sunflower.rect)
  
#grass
for i in range(100):
    x=randint(12,W)
    y=randint(12,H)
    grass=Grass(x,y)
    if grass.rect.collidelist(filled_rects)==-1:
        grasss.append(grass)
        filled_rects.append(grass.rect)
       
#weeds
for i in range(100):
    x=randint(12,W)
    y=randint(12,H)
    weed=Weed(x,y)
    if weed.rect.collidelist(filled_rects)==-1:
        weeds.append(weed)
        filled_rects.append(weed.rect)
       
#roots
for i in range(100):
    x=randint(12,W)
    y=randint(12,H)
    root=Root(x,y)
    if root.rect.collidelist(filled_rects)==-1:
        roots.append(root)
        filled_rects.append(root.rect)
#delete clear_rect from filled_rects so the farmer can walk through it
filled_rects.remove(clear_rect)
filled_rects.remove(well_rect)
#delete the bigger well_rect from filled_rects and add a smaller one that fits the image better 
well_rect_smaller=pygame.Rect(well_rect.left+1.5*TS, well_rect.top+1.3*TS-3, 1*TS, 1.4*TS)
filled_rects.append(well_rect_smaller)
title_screen=pygame.image.load('title_screen.png')

black_screen=pygame.Surface((45*TS,30*TS))
black_screen.fill((0,0,0))
darkness=0

Intro_Screen=pygame.image.load('Intro_Screen.png')
Intro_Screen_rect=pygame.Rect(0,0,720,460)

start_up=pygame.mixer.Sound('start_up_sound.mp3')

songs=['song1.mp3','song2.mp3','song3.mp3','song4.mp3']

night_songs=['songnight1.mp3','songnight2.mp3','songnight3.mp3']

leave=1
running=1
while leave:
    start_up.play()
    while running:
        screen.blit(title_screen,(0,0))
        events=pygame.event.get()
        for e in events:
            if e.type==pygame.QUIT:
                running=0
                leave=0
            if e.type==pygame.KEYDOWN:
                running=0
        pygame.display.flip()
    if leave==0:
        break
    running=1
    while running:
        black_screen.set_alpha(darkness)
        screen.blit(black_screen)
        pygame.display.flip()
        if darkness>=76:
            running=0
        else:
            darkness+=1
            ticks.tick(20)
    running=1
    while running:
        events=pygame.event.get()
        for e in events:
            if e.type==pygame.QUIT:
                running=0
                leave=0
            elif e.type==pygame.KEYDOWN:
                running=0
        screen.blit(Intro_Screen,Intro_Screen_rect)
        pygame.display.flip()
    if leave==0:
        break
    running=1
    while running:
        if farmer.darkness<68:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load(choice(songs))
                pygame.mixer.music.set_volume(.35)
                pygame.mixer.music.play()
        else:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load(choice(night_songs))
                pygame.mixer.music.set_volume(.35)
                pygame.mixer.music.play()
        #main loop
        #get current time
        time=pygame.time.get_ticks()
        #send the current time into the time class for the timer
        clock.timer(time)
        screen.blit(bg,(0,0))
        #draw the ground details and soil first since it is on the ground and want it to be in the lowest layer
        for flower_ground in flower_grounds:
            flower_ground.draw(screen)
            
        for fancy_grass in fancy_grasss:
            fancy_grass.draw(screen)
            
        for soil in soils:
            soil.draw(screen)
            
        #have the carrots go ontop of the soil
        for carrot in carrots:
            carrot.grow(time,soils)
            carrot.draw(screen)
            
        for plum in plums:
            plum.grow(time,soils)
            plum.draw(screen)
            
        for corn in corns:
            corn.grow(time,soils)
            corn.draw(screen)
            
        #draw the house and the well next
        house.draw(screen)
        well.draw(screen)
        market.draw(screen)
        #draw all the obstacles from their lists
            
        for tree in trees:
            tree.draw(screen)
        
        for rock in rocks:
            rock.draw(screen)
            
        for lil_tree in lil_trees:
            lil_tree.draw(screen)
            
        for sunflower in sunflowers:
            sunflower.draw(screen)
        
        for grass in grasss:
            grass.draw(screen)
            
        for weed in weeds:
            weed.draw(screen)
            
        for root in roots:
            root.draw(screen)
        #draw the farmer latter so he stays on the upper layers
        farmer.draw(screen,clock)
        #Have the UI drawn last so the farmer doesn't clip over it
        ax_slot.draw(screen)
        hoe_slot.draw(screen)
        water_slot.draw(screen)
        #only draw the pickaxe if it has been bought
        if market_UI.pickaxe_bought==1:
            pickaxe_slot.draw(screen)
        if market_UI.scythe_bought==1:
            scythe_slot.draw(screen)
        clock.draw(screen)
        backpack.draw(screen)
        inventory.draw(screen,farmer)
        market_UI.draw(screen,farmer,inventory)
        #flip the display
        pygame.display.flip()
        #have the farmer move method on the outside so that it can run continuously when a key is pressed
        #make it so the farmer can only move if the market and inventory menus are closed
        if inventory.inventory_open==0 and farmer.market_open==0:
            farmer.move(speed,filled_rects,screen_Rect)
        #get events
        events=pygame.event.get()
        for e in events:
            #if quit is clicked quit out the loop
            if e.type==pygame.QUIT:
                running=0
                leave=0
            #get the events for each specific method within farmer or background
            farmer.equip(e,market_UI)
            farmer.chop_tree(e,filled_rects,trees,lil_trees,roots)
            farmer.break_rock(e,filled_rects,rocks)
            farmer.slice_down(e,filled_rects,sunflowers,grasss,weeds)
            farmer.till_dirt(e,filled_rects,screen_Rect,soils)
            farmer.water_soil(e,soils,well_rect)
            farmer.Plant_carrot(e,soils,carrots,plums,corns)
            farmer.Plant_plum(e,soils,plums,carrots,corns)
            farmer.Plant_corn(e,soils,corns,plums,carrots)
            farmer.Harvest_carrot(e,carrots)
            farmer.Harvest_plum(e,plums)
            farmer.Harvest_corn(e,corns)
            backpack.mouse(e,inventory,farmer)
            farmer.Open_market(e,market,inventory)
            market_UI.mouse(e,farmer)
            inventory.mouse(e,farmer)
            farmer.go_sleep(e,door_rect,screen,ticks)
        #determines farmer speed and frame rate
        ticks.tick(20)
#quit out
pygame.quit()