import pygame
pygame.mixer.init()
#import the background file and required classes
from background import *
#create class
class Farmer:
    def __init__(self,x,y):
        #define constant
        TS=16
        #set coordinates that were inputed 
        self.x=x
        self.y=y
        #load the default forward facing image
        self.image=pygame.image.load('farmer_forward.png')
        #scale image down so it looks more natural
        self.image=pygame.transform.smoothscale(self.image, (16,16))
        #create a rectangle the size of the image and set the center equal to the coordinates
        self.rect=self.image.get_rect(center=(self.x,self.y))
        #create a default state for the tools
        self.nothing=0
        self.ax=0
        self.hoe=0
        self.water=0
        self.carrot=0
        self.plum=0
        self.corn=0
        self.pickaxe=0
        self.scythe=0
        #create a default range for the farmer to be able to interact with(if he is facing forward)
        self.DX=0
        self.DY=TS/4
        #create a direction variable with a default of facing forward
        self.direction='forward'
        #make a stamina bar the is slowly drained as the farmer does stuff
        self.stamina=100
        self.water_can=0
        self.slot=pygame.Surface((2*TS,2*TS))
        self.slot.fill((169,169,169))
        self.slot.set_alpha(140)
        #highlight the equipped slot
        self.equipped_slot=pygame.Surface((2*TS,2*TS))
        self.equipped_slot.fill((255,215,0))
        self.equipped_slot.set_alpha(100)
        #Seed Counter
        pygame.font.init()
        #get one of the default fonts that pygame has
        self.font=pygame.font.SysFont('consolas',12,bold=1)
        #set the default amount of seeds the farmer starts with
        self.carrot_seed=5
        self.plum_seed=0
        self.corn_seed=0
        #Turn to night
        self.night=pygame.Surface((45*TS,30*TS))
        self.night.fill((0,0,0))
        self.darkness=0
        #Harvested Carrots
        self.carrots_harvested=1
        self.plums_harvested=1
        self.corns_harvested=1
        #set the coordinates for the market menu
        x1=22.5*TS
        y1=15*TS
        #set the market open to false
        self.market_open=0
        self.market=pygame.image.load('market_buy_sell.png')
        self.market_rect=self.market.get_rect(center=(x1,y1))
        self.money=10
        self.energy_cans=1
        #day counter
        self.day=1
        self.fade=0
        self.day_info=0
    def draw(self,screen,clock):
        TS=16
        #make a draw class that blits the farmer and rectangle
        screen.blit(self.image,self.rect)
        #Night Time
        #set the alpha of the black screen to self.darkness
        self.night.set_alpha(self.darkness)
        #sets the darkness max to 150
        if clock.count<150:
            #makes the darkness equal to the the clock count
            self.darkness=clock.count
            #blit the dark screen only if the its past 6 PM
        if clock.hours!=12 and clock.hours>5 and clock.period=='PM':
            screen.blit(self.night,(0,0))
            #if market_open is true then blit it
        if self.market_open==1:
            screen.blit(self.market,self.market_rect)
            
        ###USER INTERFACE###
        ###Stamina Bar###
        pygame.draw.rect(screen, (0,0,0), (42*TS,3*TS-2,8,104), 2)
        pygame.draw.rect(screen, (124,252,0), (42*TS+2,3*TS+(100-self.stamina),4,self.stamina), 0)
        ###Inventory Slots###
        x_start=14.5*TS+8
        y_start=2*TS
        #The Gray Slots
        for i in range(8):
            x_coord=x_start+(i*30)
            screen.blit(self.slot,(x_coord,y_start))
        #Highlighted Spot
        if self.ax==1:
            screen.blit(self.equipped_slot,(x_start,y_start))
        elif self.hoe==1:
            screen.blit(self.equipped_slot,(x_start+30,y_start))
        elif self.water==1:
            screen.blit(self.equipped_slot,(x_start+60,y_start))
        elif self.pickaxe==1:
            screen.blit(self.equipped_slot,(x_start+90,y_start))
        elif self.scythe==1:
            screen.blit(self.equipped_slot,(x_start+120,y_start))
        elif self.carrot==1:
            screen.blit(self.equipped_slot,(x_start+150,y_start))
        elif self.plum==1:
            screen.blit(self.equipped_slot,(x_start+180,y_start))
        elif self.corn==1:
            screen.blit(self.equipped_slot,(x_start+210,y_start))
    
        #Water In Can Bar
        pygame.draw.rect(screen, (14,134,234), (x_start+66,y_start+27,self.water_can*2,2), 2)
        #Seed Slot
        screen.blit(pygame.image.load('carrot_slot.png'),(14.5*TS+158,2*TS))
        screen.blit(pygame.image.load('plum_slot.png'),(14.5*TS+188,2*TS))
        screen.blit(pygame.image.load('corn_slot.png'),(14.4*TS+218,2*TS))
        
        #Seed Counter
        #set main text with the text reading the amount of seeds and the color to white
        text_carrot=self.font.render(str(self.carrot_seed),0,(255,255,255))
        #set a shadow below it for astectics that is one pixel down and right and black
        shadow_carrot=self.font.render(str(self.carrot_seed),0,(0,0,0))
        
        text_plum=self.font.render(str(self.plum_seed),0,(255,255,255))
        shadow_plum=self.font.render(str(self.plum_seed),0,(0,0,0))
        
        text_corn=self.font.render(str(self.corn_seed),0,(255,255,255))
        shadow_corn=self.font.render(str(self.corn_seed),0,(0,0,0))
        #if the carrot count is double digits move the numbers to the right to avoid it clipping outside of the box
        if self.carrot_seed<10:
            #blit text
            screen.blit(shadow_carrot,(x_start+173,y_start+20))
            screen.blit(text_carrot,(x_start+172,y_start+19))
        else:
            screen.blit(shadow_carrot,(x_start+166,y_start+20))
            screen.blit(text_carrot,(x_start+165,y_start+19))
            
        if self.plum_seed<10:
            #blit text
            screen.blit(shadow_plum,(x_start+203,y_start+20))
            screen.blit(text_plum,(x_start+202,y_start+19))
        else:
            screen.blit(shadow_plum,(x_start+196,y_start+20))
            screen.blit(text_plum,(x_start+195,y_start+19))
            
        if self.corn_seed<10:
            #blit text
            screen.blit(shadow_corn,(x_start+233,y_start+20))
            screen.blit(text_corn,(x_start+232,y_start+19))
        else:
            screen.blit(shadow_corn,(x_start+226,y_start+20))
            screen.blit(text_corn,(x_start+225,y_start+19))
        #Outer Border
        pygame.draw.rect(screen, (0,0,0), (14.5*TS+8,2*TS,16*TS-14,2*TS), 2)
        #Each Slot Border
        for i in range(8):
            x_coord=x_start+(i*30)
            pygame.draw.rect(screen,(0,0,0),(x_coord,y_start,2*TS,2*TS),2)
        
    def farmer_look(self):
        #if ax is 1 then a variable named farmer is assigned to a string that describes what image will be called
        if self.ax==1:
            farmer='farmer_ax_'
        #same thing but with a hoe
        elif self.hoe==1:
            farmer='farmer_hoe_'
        
        elif self.water==1:
            farmer='farmer_water_'
            
        elif self.pickaxe==1:
            farmer='farmer_pickaxe_'
            
        elif self.scythe==1:
            farmer='farmer_scythe_'
        #if neither ax or hoe is 1 than the farmer variable is assigned to just a string saying
        #farmer which correlates to the default farmer appearance
        else:
            farmer='farmer_'
        #set a file path equal to the farmer's state and direction and add .png so it matched an image in my files
        #my images were named specifically so the can be easily differenciated, but also organized
        farmer_img=farmer+self.direction+'.png'
        #load the specific file path needed
        self.image=pygame.image.load(farmer_img)
        #scale image down
        self.image=pygame.transform.smoothscale(self.image, (16,16))
        
    def equip(self,e,market_UI):
        #get e type
        if self.ax==1 or self.carrot==1 or self.water==1 or self.hoe==1 or self.pickaxe==1 or self.plum==1 or self.scythe==1 or self.corn==1:
            self.nothing=1
        else:
            self.nothing=0
        if e.type==pygame.KEYDOWN:
            #if the key is a and ax is 1 already set it to 0
            if e.key==pygame.K_1:
                if self.ax==1:
                    self.ax=0
                #if it is not 1 then set it to 1 and set hoe to 0 to unequip hoe if it is equipped
                else:   
                    self.ax=1
                if self.ax==1:
                    self.hoe=0
                    self.water=0
                    self.carrot=0
                    self.plum=0
                    self.pickaxe=0
                    self.scythe=0
                    self.corn=0
                #call the farmer_look method to update how the farmer looks after a tool is equipped
                self.farmer_look()
            #same thing but with the hoe
            if e.key==pygame.K_2:
                if self.hoe==1:
                    self.hoe=0
                else:
                    self.hoe=1
                if self.hoe==1:
                    self.ax=0
                    self.plum=0
                    self.water=0
                    self.carrot=0
                    self.pickaxe=0
                    self.scythe=0
                    self.corn=0
                self.farmer_look()
                
            if e.key==pygame.K_3:
                if self.water==1:
                    self.water=0
                else:
                    self.water=1
                if self.water==1:
                    self.ax=0
                    self.hoe=0
                    self.carrot=0
                    self.plum=0
                    self.pickaxe=0
                    self.scythe=0
                    self.corn=0
                self.farmer_look()
                
            if e.key==pygame.K_4:
                if self.pickaxe==1:
                    self.pickaxe=0
                else:
                    if market_UI.pickaxe_bought==1:
                        self.pickaxe=1
                if self.pickaxe==1:
                    self.ax=0
                    self.hoe=0
                    self.plum=0
                    self.carrot=0
                    self.water=0
                    self.scythe=0
                    self.corn=0
                self.farmer_look()
                
            if e.key==pygame.K_5:
                if self.scythe==1:
                    self.scythe=0
                else:
                    if market_UI.scythe_bought==1:
                        self.scythe=1
                if self.scythe==1:
                    self.ax=0
                    self.hoe=0
                    self.plum=0
                    self.carrot=0
                    self.water=0
                    self.pickaxe=0
                    self.corn=0
                self.farmer_look()
            
            if e.key==pygame.K_6:
                if self.carrot==1:
                    self.carrot=0
                else:
                    self.carrot=1
                if self.carrot==1:
                    self.ax=0
                    self.plum=0
                    self.hoe=0
                    self.water=0
                    self.pickaxe=0
                    self.scythe=0
                    self.corn=0
                self.farmer_look()
                
            if e.key==pygame.K_7:
                if self.plum==1:
                    self.plum=0
                else:
                    self.plum=1
                if self.plum==1:
                    self.ax=0
                    self.carrot=0
                    self.hoe=0
                    self.water=0
                    self.pickaxe=0
                    self.scythe=0
                    self.corn=0
                self.farmer_look()
                
            if e.key==pygame.K_8:
                if self.corn==1:
                    self.corn=0
                else:
                    self.corn=1
                if self.corn==1:
                    self.ax=0
                    self.carrot=0
                    self.hoe=0
                    self.water=0
                    self.pickaxe=0
                    self.scythe=0
                    self.plum=0
                self.farmer_look()
                
    def move(self,speed,filled_rects,screen_Rect):
        #this method required arguments to determine speed, filled_rects to know where other objects are, and screen_rect
        #so the farmer can't walk off screen
        #define constants
        dy=0
        dx=0
        TS=16
        #if a key gets pressed down get it and set it equal to keys
        keys=pygame.key.get_pressed()
        #if the down key is pressed then itll run this function
        if keys[pygame.K_DOWN]:
            #set the direction to forward and call the farmer_look method to change where the farmer is looking
            self.direction='forward'
            self.farmer_look()
            #set a change in the direction the farmer is looking to speed
            dy=speed
            #set the hitbox infront of the farmer to a certain bound area
            self.DX=0
            self.DY=TS/4
            #repeat for each direction
        if keys[pygame.K_UP]:
            self.direction='backward'
            self.farmer_look()
            dy=-speed
            self.DX=0
            self.DY=-TS/4
        if keys[pygame.K_RIGHT]:
            self.direction='right'
            self.farmer_look()
            dx=speed
            self.DY=0
            self.DX=TS/4
        if keys[pygame.K_LEFT]:
            self.direction='left'
            self.farmer_look()
            dx=-speed
            self.DY=0
            self.DX=-TS/4
        
        #create a new rectangle that is moved slightly infront of the farmer in the direction he is facing
        new_rect=self.rect.move(dx,dy)
        #check if the new rectangle collides with anything in the filled_rects list or the edge of the screen
        if new_rect.collidelist(filled_rects)==-1 and screen_Rect.contains(new_rect):
            #if it doesnt collide then set the characters rectangle equal to the new rectangle
            self.rect=new_rect
            #then move the character to the characters rectangle
            self.x,self.y=self.rect.center
        #this method uses key inputs, filled_rects,trees,lil_trees,roots lists
    def chop_tree(self,e,filled_rects,trees,lil_trees,roots):
        ax_sound=pygame.mixer.Sound('ax_sound.mp3')
        if e.type==pygame.KEYDOWN:
            #if the space key is pressed and ax is 1
            if e.key==pygame.K_SPACE and self.ax==1:
                #stamina is checked and if stamina is greater than 0 it takes 1 away and performs the action
                if self.stamina>0:
                    self.stamina-=1
                    #create a rectangle that is in the direction the character is facing and projected out
                    ax_rect=self.rect.move(self.DX,self.DY)
                    #check the trees
                    for tree in trees:
                        #if the ax rect collides with a tree subtract that trees health by 1
                        if ax_rect.colliderect(tree.rect):
                            ax_sound.play()
                            tree.health-=1
                            if tree.health==0:
                                #if that trees health is 0 then check for the tree's rect in filled rects and remove it from the list
                                if tree.rect in filled_rects:
                                    filled_rects.remove(tree.rect)
                                #then remove the tree from the trees list and then break out the loop to avoid accidentlly hitting multiple trees at once
                                trees.remove(tree)
                            break
                        #check if the ax box hit a lil_tree then perform the same action
                    for lil_tree in lil_trees:
                        if ax_rect.colliderect(lil_tree.rect):
                            ax_sound.play()
                            if lil_tree.rect in filled_rects:
                                filled_rects.remove(lil_tree.rect)
                            lil_trees.remove(lil_tree)
                            break
                        #same with the roots
                    for root in roots:
                        if ax_rect.colliderect(root.rect):
                            ax_sound.play()
                            if root.rect in filled_rects:
                                filled_rects.remove(root.rect)
                            roots.remove(root)
                            break
               #this method uses key inputs, filled_rects, screen_rects, and the soils list
    def slice_down(self,e,filled_rects,sunflowers,grasss,weeds):
        scythe_sound=pygame.mixer.Sound('scythe_sound.mp3')
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_SPACE and self.scythe==1:
                if self.stamina>0:
                    self.stamina-=1
                    scythe_rect=self.rect.move(self.DX,self.DY)
                    scythe_sound.play()
                    for sunflower in sunflowers:
                        if scythe_rect.colliderect(sunflower.rect):
                            if sunflower.rect in filled_rects:
                                filled_rects.remove(sunflower.rect)
                            sunflowers.remove(sunflower)
                            break
                    for grass in grasss:
                        if scythe_rect.colliderect(grass.rect):
                            if grass.rect in filled_rects:
                                filled_rects.remove(grass.rect)
                            grasss.remove(grass)
                            break
                    for weed in weeds:
                        if scythe_rect.colliderect(weed.rect):
                            if weed.rect in filled_rects:
                                filled_rects.remove(weed.rect)
                            weeds.remove(weed)
                            break
    def break_rock(self,e,filled_rects,rocks):
        pickaxe_sound=pygame.mixer.Sound('pickaxe_sound.mp3')
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_SPACE and self.pickaxe==1:
                if self.stamina>0:
                    self.stamina-=1
                    pickaxe_rect=self.rect.move(self.DX,self.DY)
                    for rock in rocks:
                        if pickaxe_rect.colliderect(rock.rect):
                            pickaxe_sound.play()
                            rock.health-=1
                            if rock.health==0:
                                if rock.rect in filled_rects:
                                    filled_rects.remove(rock.rect)
                                    rocks.remove(rock)
                            break
    def till_dirt(self,e,filled_rects,screen_Rect,soils):
        plant=pygame.mixer.Sound('plant.mp3')
        #define constants
        TS=16
        if e.type==pygame.KEYDOWN:
            #if space is pressed and hoe is 1
            if e.key==pygame.K_SPACE and self.hoe==1:
                #check stamina and if it is greater than 0 subtract 1 and perform the action
                if self.stamina<=0:
                    return
                self.stamina-=1
                plant.play()
                #get the farmers x and y coordinates of the center of the rectangle
                hit_x=self.rect.centerx
                hit_y=self.rect.centery
                #depending on where the farmer is facing add a TS distance infront of the farmer
                if self.direction=='forward':
                    hit_y+=TS
                elif self.direction=='backward':
                    hit_y-=TS
                elif self.direction=='right':
                    hit_x+=TS
                elif self.direction=='left':
                    hit_x-=TS
                #create a grid that takes where the farmer hit, divides it by TS and floors it to the closes integer
                #then multiple it by TS to have it line up where the farmer is
                #this makes it so that the tilled dirt can be set up in an organized grid pattern
                grid_x=int(hit_x//TS)*TS
                grid_y=int(hit_y//TS)*TS
                #create a rectangle that is where the farmer tilled the ground
                hit_rect=pygame.Rect(grid_x,grid_y,TS,TS)
                #if there is already soil there then this prevents it from putting another soil ontop of it
                for soil in soils:
                    if soil.rect.topleft==(grid_x,grid_y):
                        return
                #check if the soil rectangle collides with anything, if not then add a Soil instant to the soil list
                #at the specific spot in the grid
                if hit_rect.collidelist(filled_rects)==-1:
                    soils.append(Soil(grid_x,grid_y))
                    #using dictionary comprehension to get the top left corner of each soil block in soils list
                    soil_map={soil.rect.topleft: soil for soil in soils}
                    #then take each soil and get their x and y coordinates, then check if there is a soil above or below
                    #each soil in the list by checking if there is a matching coordinate within the dictionary
                    #if there is it returns True
                    for soil in soils:
                        x,y=soil.rect.topleft
                        above=(x,y-TS) in soil_map
                        below=(x,y+TS) in soil_map
                        #the resulting true or falses are then sent to the method in background to constantly update each
                        #soil tile that is placed
                        soil.updated_soil(above,below)
    
    def water_soil(self,e,soils,well_rect):
        TS=16
        water_sound=pygame.mixer.Sound('water_sound.mp3')
        well_sound=pygame.mixer.Sound('well_sound.mp3')
        if e.type==pygame.KEYDOWN:
            #if space is pressed and hoe is 1
            if e.key==pygame.K_SPACE and self.water==1:
                #check stamina and if it is greater than 0 subtract 1 and perform the action
                if self.stamina<=0:
                    return
                self.stamina-=1
                
                #get the farmers x and y coordinates of the center of the rectangle
                hit_x=self.rect.centerx
                hit_y=self.rect.centery
                #depending on where the farmer is facing add a TS distance infront of the farmer
                if self.direction=='forward':
                    hit_y+=TS
                elif self.direction=='backward':
                    hit_y-=TS
                elif self.direction=='right':
                    hit_x+=TS
                elif self.direction=='left':
                    hit_x-=TS
                grid_x=int(hit_x//TS)*TS
                grid_y=int(hit_y//TS)*TS
                #create a rectangle that is where the farmer tilled the ground
                hit_rect=pygame.Rect(grid_x,grid_y,TS,TS)
                if hit_rect.colliderect(well_rect):
                    self.water_can=10
                    well_sound.play()
                else:
                    if self.water_can>0:
                        self.water_can-=1
                        water_sound.play()
                        for soil in soils:
                            if hit_rect.colliderect(soil.rect):
                                soil.soil_water=1
                                soil.updated_soil(soil.above,soil.below)
                                break
                            
    def Plant_carrot(self,e,soils,carrots,plums,corns):
        TS=16
        if e.type==pygame.KEYDOWN:
            #if space is pressed and hoe is 1
            if e.key==pygame.K_SPACE and self.carrot==1:
                #check stamina and if it is greater than 0 subtract 1 and perform the action
                if self.stamina<=0:
                    return
                self.stamina-=1
                
                hit_x=self.rect.centerx
                hit_y=self.rect.centery
                #depending on where the farmer is facing add a TS distance infront of the farmer
                if self.direction=='forward':
                    hit_y+=TS
                elif self.direction=='backward':
                    hit_y-=TS
                elif self.direction=='right':
                    hit_x+=TS
                elif self.direction=='left':
                    hit_x-=TS
                grid_x=int(hit_x//TS)*TS
                grid_y=int(hit_y//TS)*TS
                #create a rectangle that is where the farmer is trying to plant
                hit_rect=pygame.Rect(grid_x,grid_y,TS,TS)
                # if a carrot already exists where the farmer is trying to plant end the action
                for carrot in carrots:
                    if carrot.rect.topleft==(grid_x,grid_y):
                        return
                    
                for plum in plums:
                    if plum.rect.topleft==(grid_x,grid_y):
                        return
                    
                for corn in corns:
                    if corn.rect.topleft==(grid_x,grid_y):
                        return
                #if the carrot hit_box falls onto a soil rect then plant the carrot in the grid spot
                #by calling an instance of the class and subtract one from the amount of seeds left
                for soil in soils:   
                    if hit_rect.colliderect(soil.rect):
                        if self.carrot_seed>0:
                            self.carrot_seed-=1
                            carrots.append(Carrot(grid_x,grid_y))
                            
    def Plant_plum(self,e,soils,plums,carrots,corns):
        TS=16
        if e.type==pygame.KEYDOWN:
            #if space is pressed and hoe is 1
            if e.key==pygame.K_SPACE and self.plum==1:
                #check stamina and if it is greater than 0 subtract 1 and perform the action
                if self.stamina<=0:
                    return
                self.stamina-=1
                
                hit_x=self.rect.centerx
                hit_y=self.rect.centery
                #depending on where the farmer is facing add a TS distance infront of the farmer
                if self.direction=='forward':
                    hit_y+=TS
                elif self.direction=='backward':
                    hit_y-=TS
                elif self.direction=='right':
                    hit_x+=TS
                elif self.direction=='left':
                    hit_x-=TS
                grid_x=int(hit_x//TS)*TS
                grid_y=int(hit_y//TS)*TS
                #create a rectangle that is where the farmer is trying to plant
                hit_rect=pygame.Rect(grid_x,grid_y,TS,TS)
                # if a carrot already exists where the farmer is trying to plant end the action
                for plum in plums:
                    if plum.rect.topleft==(grid_x,grid_y):
                        return
                    
                for carrot in carrots:
                    if carrot.rect.topleft==(grid_x,grid_y):
                        return
                    
                for corn in corns:
                    if corn.rect.topleft==(grid_x,grid_y):
                        return
                #if the carrot hit_box falls onto a soil rect then plant the carrot in the grid spot
                #by calling an instance of the class and subtract one from the amount of seeds left
                for soil in soils:   
                    if hit_rect.colliderect(soil.rect):
                        if self.plum_seed>0:
                            self.plum_seed-=1
                            plums.append(Plum(grid_x,grid_y))
                            
    def Plant_corn(self,e,soils,corns,plums,carrots):
        TS=16
        if e.type==pygame.KEYDOWN:
            #if space is pressed and hoe is 1
            if e.key==pygame.K_SPACE and self.corn==1:
                #check stamina and if it is greater than 0 subtract 1 and perform the action
                if self.stamina<=0:
                    return
                self.stamina-=1
                
                hit_x=self.rect.centerx
                hit_y=self.rect.centery
                #depending on where the farmer is facing add a TS distance infront of the farmer
                if self.direction=='forward':
                    hit_y+=TS
                elif self.direction=='backward':
                    hit_y-=TS
                elif self.direction=='right':
                    hit_x+=TS
                elif self.direction=='left':
                    hit_x-=TS
                grid_x=int(hit_x//TS)*TS
                grid_y=int(hit_y//TS)*TS
                #create a rectangle that is where the farmer is trying to plant
                hit_rect=pygame.Rect(grid_x,grid_y,TS,TS)
                # if a carrot already exists where the farmer is trying to plant end the action
                for plum in plums:
                    if plum.rect.topleft==(grid_x,grid_y):
                        return
                    
                for carrot in carrots:
                    if carrot.rect.topleft==(grid_x,grid_y):
                        return
                    
                for corn in corns:
                    if corn.rect.topleft==(grid_x,grid_y):
                        return
                #if the carrot hit_box falls onto a soil rect then plant the carrot in the grid spot
                #by calling an instance of the class and subtract one from the amount of seeds left
                for soil in soils:   
                    if hit_rect.colliderect(soil.rect):
                        if self.corn_seed>0:
                            self.corn_seed-=1
                            corns.append(Corn(grid_x,grid_y))
                            
    def Harvest_carrot(self,e,carrots):
        harvest_sound=pygame.mixer.Sound('harvest_sound.mp3')
        TS=16
        #if the space key is pressed and the player is holding nothing
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_SPACE and self.nothing==0:
                #take away from the stamina
                if self.stamina<=0:
                    return
                self.stamina-=1
                #get where the player is facing and one tile infront of them
                hit_x=self.rect.centerx
                hit_y=self.rect.centery
                if self.direction=='forward':
                    hit_y+=TS
                elif self.direction=='backward':
                    hit_y-=TS
                elif self.direction=='right':
                    hit_x+=TS
                elif self.direction=='left':
                    hit_x-=TS
                grid_x=int(hit_x//TS)*TS
                grid_y=int(hit_y//TS)*TS
                hit_rect=pygame.Rect(grid_x,grid_y,TS,TS)
                #if the player interacts with a carrot and the carrot is at growth stage 2 then remove the carrot
                #also add one to the amount of carrots harvested
                for carrot in carrots:
                    if hit_rect.colliderect(carrot.rect):
                        if carrot.growth==2:
                            harvest_sound.play()
                            carrots.remove(carrot)
                            self.carrots_harvested+=1
                            
    def Harvest_plum(self,e,plums):
        harvest_sound=pygame.mixer.Sound('harvest_sound.mp3')
        TS=16
        #if the space key is pressed and the player is holding nothing
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_SPACE and self.nothing==0:
                #take away from the stamina
                if self.stamina<=0:
                    return
                self.stamina-=1
                #get where the player is facing and one tile infront of them
                hit_x=self.rect.centerx
                hit_y=self.rect.centery
                if self.direction=='forward':
                    hit_y+=TS
                elif self.direction=='backward':
                    hit_y-=TS
                elif self.direction=='right':
                    hit_x+=TS
                elif self.direction=='left':
                    hit_x-=TS
                grid_x=int(hit_x//TS)*TS
                grid_y=int(hit_y//TS)*TS
                hit_rect=pygame.Rect(grid_x,grid_y,TS,TS)
                #if the player interacts with a carrot and the carrot is at growth stage 2 then remove the carrot
                #also add one to the amount of carrots harvested
                for plum in plums:
                    if hit_rect.colliderect(plum.rect):
                        if plum.growth==2:
                            harvest_sound.play()
                            plums.remove(plum)
                            self.plums_harvested+=1
                            
    def Harvest_corn(self,e,corns):
        harvest_sound=pygame.mixer.Sound('harvest_sound.mp3')
        TS=16
        #if the space key is pressed and the player is holding nothing
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_SPACE and self.nothing==0:
                #take away from the stamina
                if self.stamina<=0:
                    return
                self.stamina-=1
                #get where the player is facing and one tile infront of them
                hit_x=self.rect.centerx
                hit_y=self.rect.centery
                if self.direction=='forward':
                    hit_y+=TS
                elif self.direction=='backward':
                    hit_y-=TS
                elif self.direction=='right':
                    hit_x+=TS
                elif self.direction=='left':
                    hit_x-=TS
                grid_x=int(hit_x//TS)*TS
                grid_y=int(hit_y//TS)*TS
                hit_rect=pygame.Rect(grid_x,grid_y,TS,TS)
                #if the player interacts with a carrot and the carrot is at growth stage 2 then remove the carrot
                #also add one to the amount of carrots harvested
                for corn in corns:
                    if hit_rect.colliderect(corn.rect):
                        if corn.growth==2:
                            harvest_sound.play()
                            corns.remove(corn)
                            self.corns_harvested+=1
                            
    def Open_market(self,e,market,inventory):
        TS=16
        #if the space key is pressed and the player is nothing
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_SPACE and self.nothing==0:
                hit_x=self.rect.centerx
                hit_y=self.rect.centery
                if self.direction=='backward':
                    hit_y-=TS
                grid_x=int(hit_x//TS)*TS
                grid_y=int(hit_y//TS)*TS
                hit_rect=pygame.Rect(grid_x,grid_y,TS,TS)
                if hit_rect.colliderect(market.rect):
                    #if the player interacts with the market then open it
                    if self.market_open==0:
                        self.market_open=1
                        inventory.inventory_open=0
                        #if the market is already open then close it
                    else:
                        self.market_open=0
                        
    def go_sleep(self,e,door_rect,screen,ticks):
        TS=16
        self.night.set_alpha(self.fade)
        screen.blit(self.night,(0,0))
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_SPACE and self.nothing==0:
                hit_x=self.rect.centerx
                hit_y=self.rect.centery
                if self.direction=='backward':
                    hit_y-=TS
                grid_x=int(hit_x//TS)*TS
                grid_y=int(hit_y//TS)*TS
                hit_rect=pygame.Rect(grid_x,grid_y,TS,TS)
                if hit_rect.colliderect(door_rect):
                    print('Go to next Day')
                
    
                    
