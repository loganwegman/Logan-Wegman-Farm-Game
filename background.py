import pygame
class House:
    def __init__(self):
        #define TS
        TS=16
        #create rectangle and allow center to be set
        self.rect=pygame.Rect(0,0,3*TS,6*TS)
        self.rect.center=(150,250)
        #let image be the rectange with background removed
        self.image=pygame.Surface(self.rect.size, pygame.SRCALPHA)
        
    def Barn(self):
        TS=16
        TS1=17
        #load tile_sheet
        tile_sheet=pygame.image.load('tilemap.png')
        #blit each part if the barn onto the rectangle
        wall1=(7*TS1,7*TS1,TS,TS)
        self.image.blit(tile_sheet,(0*TS,4*TS),wall1)
        self.image.blit(tile_sheet,(1*TS,4*TS),wall1)
        self.image.blit(tile_sheet,(2*TS,4*TS),wall1)

        wall2=(7*TS1,9*TS1,TS,TS)
        self.image.blit(tile_sheet,(1*TS,3*TS),wall2)

        wall3=(6*TS1,9*TS1,TS,TS)
        self.image.blit(tile_sheet,(0*TS,5*TS),wall3)

        wall4=(8*TS1,9*TS1,TS,TS)
        self.image.blit(tile_sheet,(2*TS,5*TS),wall4)

        door=(7*TS1,10*TS1,TS,TS)
        self.image.blit(tile_sheet,(1*TS,5*TS),door)

        roof1=(10*TS1,TS1*6,TS,TS)
        self.image.blit(tile_sheet,(1*TS,0*TS),roof1)

        roof2=(10*TS1,TS1*7,TS,TS)
        self.image.blit(tile_sheet,(1*TS,1*TS),roof2)

        roof3=(9*TS1,TS1*7,TS,TS)
        self.image.blit(tile_sheet,(0*TS,1*TS),roof3)

        roof4=(11*TS1,TS1*7,TS,TS)
        self.image.blit(tile_sheet,(2*TS,1*TS),roof4)

        roof5=(10*TS1,TS1*8,TS,TS)
        self.image.blit(tile_sheet,(1*TS,2*TS),roof5)

        roof6=(9*TS1,TS1*8,TS,TS)
        self.image.blit(tile_sheet,(0*TS,2*TS),roof6)

        roof7=(11*TS1,TS1*8,TS,TS)
        self.image.blit(tile_sheet,(2*TS,2*TS),roof7)

        roof8=(10*TS1,TS1*9,TS,TS)
        self.image.blit(tile_sheet,(1*TS,3*TS),roof8)

        roof9=(9*TS1,TS1*9,TS,TS)
        self.image.blit(tile_sheet,(0*TS,3*TS),roof9)

        roof10=(11*TS1,TS1*9,TS,TS)
        self.image.blit(tile_sheet,(2*TS,3*TS),roof10)

        roof11=(9*TS1,TS1*10,TS,TS)
        self.image.blit(tile_sheet,(0*TS,4*TS),roof11)

        roof12=(11*TS1,TS1*10,TS,TS)
        self.image.blit(tile_sheet,(2*TS,4*TS),roof12)

        roof13=(10*TS1,TS1*10,TS,TS)
        self.image.blit(tile_sheet,(1*TS,4*TS),roof13)
    def draw(self,screen):
        #draw image to screen
        screen.blit(self.image,self.rect)

class Tree:
    def __init__(self,x,y):
        #define constants
        TS=16
        TS1=17
        #set a tree health so tree must be hit 3 times to break
        self.health=3
        #create a rectangle for the tree
        self.rect=pygame.Rect(0,0,1*TS,2*TS)
        #set the tree rectangle center to where it is called to be by the instance
        self.rect.center=(x,y)
        #make the image the size of the rectangle and remove background
        self.image=pygame.Surface(self.rect.size, pygame.SRCALPHA)
        #get tree from the tile sheet and blit it to the rectangle
        tree_top=(TS1*3,0*TS1,TS,TS)
        tree_bottom=(TS1*3,1*TS1,TS,TS)
        tile_sheet=pygame.image.load('tilemap.png')
        self.image.blit(tile_sheet,(0*TS,1*TS),tree_bottom)
        self.image.blit(tile_sheet,(0*TS,0*TS),tree_top)
    def draw(self,screen):
        #draw image to screen
        screen.blit(self.image,self.rect)

class Rock:
    def __init__(self,x,y):
        #repeat the same thing for each class, but adjust the image and rectangle size
        TS=16
        TS1=17
        self.health=2
        self.rect=pygame.Rect(0,0,1*TS,1*TS)
        self.rect.center=(x,y)
        self.image=pygame.Surface(self.rect.size, pygame.SRCALPHA)
        rock=(TS1*5,7*TS1,TS,TS)
        tile_sheet=pygame.image.load('tilemap.png')
        self.image.blit(tile_sheet,(0*TS,0*TS),rock)
    def draw(self,screen):
        #draw image to screen
        screen.blit(self.image,self.rect)

class Lil_Tree:
    def __init__(self,x,y):
        TS=16
        TS1=17
        self.rect=pygame.Rect(0,0,1*TS,1*TS)
        self.rect.center=(x,y)
        self.image=pygame.Surface(self.rect.size, pygame.SRCALPHA)
        lil_tree=(TS1*3,TS1*2,TS,TS)
        tile_sheet=pygame.image.load('tilemap.png')
        self.image.blit(tile_sheet,(0*TS,0*TS),lil_tree)
    def draw(self,screen):
        #draw image to screen
        screen.blit(self.image,self.rect)
        
class Sunflower:
    def __init__(self,x,y):
        TS=16
        TS1=17
        self.rect=pygame.Rect(0,0,1*TS,1*TS)
        self.rect.center=(x,y)
        self.image=pygame.Surface(self.rect.size, pygame.SRCALPHA)
        sunflower=(TS1*11,TS1*6,TS,TS)
        tile_sheet=pygame.image.load('tilemap.png')
        self.image.blit(tile_sheet,(0*TS,0*TS),sunflower)
    def draw(self,screen):
        #draw image to screen
        screen.blit(self.image,self.rect)
        
class Grass:
    def __init__(self,x,y):
        TS=16
        TS1=17
        self.rect=pygame.Rect(0,0,1*TS,1*TS)
        self.rect.center=(x,y)
        self.image=pygame.Surface(self.rect.size, pygame.SRCALPHA)
        grass=(TS1*8,TS1*6,TS,TS)
        tile_sheet=pygame.image.load('tilemap.png')
        self.image.blit(tile_sheet,(0*TS,0*TS),grass)
    def draw(self,screen):
        #draw image to screen
        screen.blit(self.image,self.rect)
        
class Weed:
    def __init__(self,x,y):
        TS=16
        TS1=17
        self.rect=pygame.Rect(0,0,1*TS,1*TS)
        self.rect.center=(x,y)
        self.image=pygame.Surface(self.rect.size, pygame.SRCALPHA)
        weed=(TS1*4,TS1*5,TS,TS)
        tile_sheet=pygame.image.load('tilemap.png')
        self.image.blit(tile_sheet,(0*TS,0*TS),weed)
    def draw(self,screen):
        #draw image to screen
        screen.blit(self.image,self.rect)
        
class Root:
    def __init__(self,x,y):
        TS=16
        TS1=17
        self.rect=pygame.Rect(0,0,1*TS,1*TS)
        self.rect.center=(x,y)
        self.image=pygame.Surface(self.rect.size, pygame.SRCALPHA)
        root=(TS1*7,TS1*5,TS,TS)
        tile_sheet=pygame.image.load('tilemap.png')
        self.image.blit(tile_sheet,(0*TS,0*TS),root)
    def draw(self,screen):
        #draw image to screen
        screen.blit(self.image,self.rect)
        
class Well:
    def __init__(self):
        #set well location to a specific spot
        TS=16
        x=35*TS
        y=5*TS
        #load the well image and create a rectangle around the image with the center at the set location
        self.image=pygame.image.load('well.png')
        self.rect=self.image.get_rect(center=(x,y))
    def draw(self,screen):
        screen.blit(self.image,self.rect)

class Market:
    def __init__(self):
        #set well location to a specific spot
        TS=16
        x=37*TS
        y=23*TS
        #load the well image and create a rectangle around the image with the center at the set location
        self.image=pygame.image.load('market.png')
        self.image_rect=self.image.get_rect(center=(x,y))
        self.rect=pygame.Rect(573,347,38,32)
    def draw(self,screen):
        screen.blit(self.image,self.image_rect)

class Soil:
    def __init__(self,x,y):
        #constants
        self.TS=16
        self.TS1=17
        #set a rectangle at the spot it is called to be at
        self.rect=pygame.Rect(x,y,self.TS,self.TS)
        self.image=pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.tile_sheet=pygame.image.load('tilemap.png')
        self.soil_water=0
        self.updated_soil(above=False,below=False)
        
    def updated_soil(self,above,below):
        #get the above and below information from the instance
        self.above=above
        self.below=below
        #depending on whether the soil is watered and if above or below is true or false in different combos
        #set soil tile equal to the respective image on the tile sheet
        if not above and not below:
            if self.soil_water==1:
                soil=(self.TS1,0,self.TS,self.TS)
            else:
                soil=(0,0,self.TS,self.TS)
            
        elif not above and below:
            if self.soil_water==1:
                soil=(self.TS1,self.TS1,self.TS,self.TS)
            else:
                soil=(0,self.TS1,self.TS,self.TS)
        elif above and below:
            if self.soil_water==1:
                soil=(self.TS1,2*self.TS1,self.TS,self.TS)
            else:
                soil=(0,2*self.TS1,self.TS,self.TS)
        elif above and not below:
            if self.soil_water==1:
                soil=(self.TS1,3*self.TS1,self.TS,self.TS)
            else:
                soil=(0,3*self.TS1,self.TS,self.TS)
        #blit the image
        self.image.blit(self.tile_sheet, (0,0),soil)
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        
        
class Flower_ground:
    def __init__(self,x,y):
        TS=16
        TS1=17
        self.image=pygame.image.load('flower_ground.png')
        self.rect=self.image.get_rect(topleft=(x,y))
    def draw(self,screen):
        #draw image to screen
        screen.blit(self.image,self.rect)
        
class Fancy_grass:
    def __init__(self,x,y):
        TS=16
        TS1=17
        self.image=pygame.image.load('fancy_grass.png')
        self.rect=self.image.get_rect(topleft=(x,y))
    def draw(self,screen):
        #draw image to screen
        screen.blit(self.image,self.rect)
        
class Ax_slot:
    def __init__(self):
        TS=16
        self.image=pygame.image.load('ax_slot.png')
        self.rect=self.image.get_rect(topleft=(14.5*TS+8,2*TS))
    def draw(self,screen):
        #draw image to screen
        screen.blit(self.image,self.rect)


class Hoe_slot:
    def __init__(self):
        TS=16
        self.image=pygame.image.load('hoe_slot.png')
        self.rect=self.image.get_rect(topleft=(14.5*TS+8+30,2*TS))
    def draw(self,screen):
        #draw image to screen
        screen.blit(self.image,self.rect)
        
class Water_slot:
    def __init__(self):
        TS=16
        self.image=pygame.image.load('water_slot.png')
        self.rect=self.image.get_rect(topleft=(14.5*TS+8+60,2*TS))
    def draw(self,screen):
        #draw image to screen
        screen.blit(self.image,self.rect)
        
class Pickaxe_slot:
    def __init__(self):
        TS=16
        self.image=pygame.image.load('pickaxe_slot.png')
        self.rect=self.image.get_rect(topleft=(14.5*TS+8+90,2*TS))
    def draw(self,screen):
        #draw image to screen
        screen.blit(self.image,self.rect)
        
class Scythe_slot:
    def __init__(self):
        TS=16
        self.image=pygame.image.load('scythe_slot.png')
        self.rect=self.image.get_rect(topleft=(14.5*TS+8+120,2*TS))
    def draw(self,screen):
        #draw image to screen
        screen.blit(self.image,self.rect)
        
class Carrot:
    def __init__(self,x,y):
        #load image
        self.TS=16
        self.TS1=17
        self.rect=pygame.Rect(x,y,self.TS,self.TS)
        self.image=pygame.Surface(self.rect.size,pygame.SRCALPHA)
        self.tile_sheet=pygame.image.load('tilemap.png')
        #set growth stage to 0
        self.growth=0
        self.plant_time=0
        #set how long it takes to grow 
        self.time_growth=3*60*1000
        #set if the carrot is watered to false
        self.carrot_watered=0
        #update the carrot so that the correct tile is used
        self.carrot_update()
        
    def carrot_update(self):
        #depending on the growth stage a different carrot png is used
        if self.growth==0:
            tile=(4*self.TS1,0,self.TS,self.TS)
        elif self.growth==1:
            tile=(5*self.TS1,0,self.TS,self.TS)
        else:
            tile=(6*self.TS1,0,self.TS,self.TS)
        #blit the carrot
        self.image.blit(self.tile_sheet,(0,0),tile)
        
    def grow(self,time,soils):
        #check if the soil is watered and if it is then make carrot_watered true
        for soil in soils:
            if self.rect.colliderect(soil.rect):
                if soil.soil_water==1:
                    self.carrot_watered=1
        #check if the carrot is watered, if it is check if the current time and the time it was last updated is longer than the time it grow
        if self.carrot_watered==1:
            #also check the growth stage so the growth counter doesn't keep going up
            if time-self.plant_time>=self.time_growth and self.growth<2:
                #once the time is long enough, grow the carrot by 1, reset the plant time, and update the carrot
                self.growth+=1
                self.plant_time=time
                self.carrot_update()
        else:
            #if the carrot isn't watered then keep the frozen by setting the plant time equal to the time
            self.plant_time=time
            
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        
class Plum:
    def __init__(self,x,y):
        #load image
        self.TS=16
        self.TS1=17
        self.rect=pygame.Rect(x,y,self.TS,self.TS)
        self.image=pygame.Surface(self.rect.size,pygame.SRCALPHA)
        self.tile_sheet=pygame.image.load('tilemap.png')
        #set growth stage to 0
        self.growth=0
        self.plant_time=0
        #set how long it takes to grow 
        self.time_growth=5*60*1000
        #set if the carrot is watered to false
        self.plum_watered=0
        #update the carrot so that the correct tile is used
        self.plum_update()
        
    def plum_update(self):
        #depending on the growth stage a different carrot png is used
        if self.growth==0:
            tile=(4*self.TS1,self.TS1,self.TS,self.TS)
        elif self.growth==1:
            tile=(5*self.TS1,self.TS1,self.TS,self.TS)
        else:
            tile=(6*self.TS1,self.TS1,self.TS,self.TS)
        #blit the carrot
        self.image.blit(self.tile_sheet,(0,0),tile)
        
    def grow(self,time,soils):
        #check if the soil is watered and if it is then make carrot_watered true
        for soil in soils:
            if self.rect.colliderect(soil.rect):
                if soil.soil_water==1:
                    self.plum_watered=1
        #check if the carrot is watered, if it is check if the current time and the time it was last updated is longer than the time it grow
        if self.plum_watered==1:
            #also check the growth stage so the growth counter doesn't keep going up
            if time-self.plant_time>=self.time_growth and self.growth<2:
                #once the time is long enough, grow the carrot by 1, reset the plant time, and update the carrot
                self.growth+=1
                self.plant_time=time
                self.plum_update()
        else:
            #if the carrot isn't watered then keep the frozen by setting the plant time equal to the time
            self.plant_time=time
            
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        
        
class Corn:
    def __init__(self,x,y):
        #load image
        self.TS=16
        self.TS1=17
        self.rect=pygame.Rect(x,y,self.TS,self.TS)
        self.image=pygame.Surface(self.rect.size,pygame.SRCALPHA)
        self.tile_sheet=pygame.image.load('tilemap.png')
        #set growth stage to 0
        self.growth=0
        self.plant_time=0
        #set how long it takes to grow 
        self.time_growth=6*60*1000
        #set if the carrot is watered to false
        self.corn_watered=0
        #update the carrot so that the correct tile is used
        self.corn_update()
        
    def corn_update(self):
        #depending on the growth stage a different carrot png is used
        if self.growth==0:
            tile=(4*self.TS1,self.TS1*2,self.TS,self.TS)
        elif self.growth==1:
            tile=(5*self.TS1,self.TS1*2,self.TS,self.TS)
        else:
            tile=(6*self.TS1,self.TS1*2,self.TS,self.TS)
        #blit the carrot
        self.image.blit(self.tile_sheet,(0,0),tile)
        
    def grow(self,time,soils):
        #check if the soil is watered and if it is then make carrot_watered true
        for soil in soils:
            if self.rect.colliderect(soil.rect):
                if soil.soil_water==1:
                    self.corn_watered=1
        #check if the carrot is watered, if it is check if the current time and the time it was last updated is longer than the time it grow
        if self.corn_watered==1:
            #also check the growth stage so the growth counter doesn't keep going up
            if time-self.plant_time>=self.time_growth and self.growth<2:
                #once the time is long enough, grow the carrot by 1, reset the plant time, and update the carrot
                self.growth+=1
                self.plant_time=time
                self.corn_update()
        else:
            #if the carrot isn't watered then keep the frozen by setting the plant time equal to the time
            self.plant_time=time
            
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        
class Clock:
    def __init__(self):
        #set the default time
        self.hours=6
        self.minutes_ten=0
        self.minutes_one=0
        self.period='AM'
        #start the timer
        self.past_time=0
        #set a font
        self.font=pygame.font.SysFont('consolas',18,bold=1)
        #start a counter that determines when the game turns dark
        self.count=0
    def timer(self,current_time):
        #check if current time minus past_time is longer than one second
        if current_time-self.past_time>=1000:
            #if it is reset past time back to current time
            self.past_time=current_time
            #add one to the in_game minutes counter
            self.minutes_one+=1
            #once the timer is past 6PM start the counter so the game starts to turn dark
            if self.hours>5 and self.hours!=12 and self.period=='PM':
                self.past_time=current_time
                self.count+=1
            #make it so that the timer works properly and switches to PM once it hits noon
        if self.minutes_one>9:
            self.minutes_ten+=1
            self.minutes_one=0
        if self.minutes_ten>5:
            self.hours+=1
            self.minutes_ten=0
        if self.hours>11:
            self.period='PM'
        if self.hours>12:
            self.hours=1
        
    def draw(self,screen):
        TS=16
        #outline of timer
        pygame.draw.rect(screen, (169,169,169), (40*TS-8,1*TS,78,20), 0)
        pygame.draw.rect(screen, (0,0,0), (40*TS-8,1*TS,78,20), 2)
        #hours
        hour_shadow=self.font.render(str(self.hours),0,(0,0,0))
        hour=self.font.render(str(self.hours),0,(255,255,255))
        #colon
        colon_shadow=self.font.render(':',0,(0,0,0))
        colon=self.font.render(':',0,(255,255,255))
        #minutes tens
        minute_ten_shadow=self.font.render(str(self.minutes_ten),0,(0,0,0))
        minute_ten=self.font.render(str(self.minutes_ten),0,(255,255,255))
        #minutes one
        minute_one_shadow=self.font.render(str(self.minutes_one),0,(0,0,0))
        minute_one=self.font.render(str(self.minutes_one),0,(255,255,255))
        #morning or afternoon
        period_shadow=self.font.render(self.period,0,(0,0,0))
        period=self.font.render(self.period,0,(255,255,255))
        #set the hours so that if it is double digits it is placed in the right spot
        if self.hours<10:
            #blit text
            screen.blit(hour_shadow,(40*TS+4,1*TS+2))
            screen.blit(hour,(40*TS+3,1*TS+1))
        else:
            screen.blit(hour_shadow,(40*TS-5,1*TS+2))
            screen.blit(hour,(40*TS-6,1*TS+1))
        #blit the rest of the timer onto the screen
        screen.blit(colon_shadow,(40*TS+14,1*TS+2))
        screen.blit(colon,(40*TS+13,1*TS+1))
        screen.blit(minute_ten_shadow,(40*TS+24,1*TS+2))
        screen.blit(minute_ten,(40*TS+23,1*TS+1))
        screen.blit(minute_one_shadow,(40*TS+35,1*TS+2))
        screen.blit(minute_one,(40*TS+34,1*TS+1))
        screen.blit(period_shadow,(40*TS+47,1*TS+2))
        screen.blit(period,(40*TS+46,1*TS+1))
        
class Backpack:
    def __init__(self):
        TS=16
        x=3*TS
        y=3*TS
        #load the well image and create a rectangle around the image with the center at the set location
        self.image=pygame.image.load('backpack.png')
        self.rect=self.image.get_rect(center=(x,y))
    def mouse(self,e,inventory,farmer):
        #get the position of the mouse and see if it collides with the backpack rect
        if e.type==pygame.MOUSEMOTION:
            if self.rect.collidepoint(e.pos):
                #if it does change the image to one that is highlighted to show that it is being selected
                self.image=pygame.image.load('backpack_highlighted.png')
            else:
                self.image=pygame.image.load('backpack.png')
                #if the mouse button is pushed down and the position is on the backpack, set open inventory to true
        if e.type==pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(e.pos) and farmer.market_open==0:
                if inventory.inventory_open==0:
                    inventory.inventory_open=1
                else:
                    inventory.inventory_open=0
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        
class Inventory:
    def __init__(self):
        self.TS=16
        #Inventory UI
        x=22.5*self.TS
        y=15*self.TS
        self.image=pygame.image.load('inventory.png')
        self.rect=self.image.get_rect(center=(x,y))
        #set the inventory to closed
        self.inventory_open=0
        #first slot in the open inventory
        #slot1
        x1=12*self.TS+3
        y1=12*self.TS+2
        
        self.carrot=pygame.image.load('carrot_inventory.png')
        self.plum=pygame.image.load('plum_inventory.png')
        self.corn=pygame.image.load('corn_inventory.png')
        self.energy=pygame.image.load('energy_inventory.png')
        self.energy=pygame.transform.smoothscale(self.energy, (24,24))
        self.energy_info=pygame.image.load('energy_info.png')
        
        self.slot_1_coords=x1,y1
        self.slot_2_coords=x1+32,y1
        self.slot_3_coords=x1+64,y1
        self.slot_4_coords=x1+96,y1
        
        self.energy_coords_1=x1,y1+27
        self.energy_coords_2=x1+32,y1+27
        self.energy_coords_3=x1+64,y1+27
        self.energy_coords_4=x1+96,y1+27
        
        self.carrot_inventory=self.carrot.get_rect(center=(self.slot_1_coords))
        
        self.plum_inventory1=self.plum.get_rect(center=(self.slot_1_coords))
        self.plum_inventory2=self.plum.get_rect(center=(self.slot_2_coords))
        
        self.corn_inventory1=self.corn.get_rect(center=(self.slot_1_coords))
        self.corn_inventory2=self.corn.get_rect(center=(self.slot_2_coords))
        self.corn_inventory3=self.corn.get_rect(center=(self.slot_3_coords))
        
        self.energy_inventory1=self.energy.get_rect(center=(self.slot_1_coords))
        self.energy_inventory2=self.energy.get_rect(center=(self.slot_2_coords))
        self.energy_inventory3=self.energy.get_rect(center=(self.slot_3_coords))
        self.energy_inventory4=self.energy.get_rect(center=(self.slot_4_coords))
        
        self.energy_info1=self.energy_info.get_rect(center=(self.energy_coords_1))
        self.energy_info2=self.energy_info.get_rect(center=(self.energy_coords_2))
        self.energy_info3=self.energy_info.get_rect(center=(self.energy_coords_3))
        self.energy_info4=self.energy_info.get_rect(center=(self.energy_coords_4))
        
        self.energy_slot=0
        self.energy_info_display=0
        
        #Info Displaying
        pygame.font.init()
        #set font
        self.font=pygame.font.SysFont('consolas',12,bold=1)
        self.big_font=pygame.font.SysFont('consolas',20)
    def draw(self,screen,farmer):
        #create the text
        text_carrot=self.font.render(str(farmer.carrots_harvested),0,(255,255,255))
        #have a shadow to make the text look nicer
        shadow_carrot=self.font.render(str(farmer.carrots_harvested),0,(0,0,0))
        
        text_plum=self.font.render(str(farmer.plums_harvested),0,(255,255,255))
        shadow_plum=self.font.render(str(farmer.plums_harvested),0,(0,0,0))
        
        text_corn=self.font.render(str(farmer.corns_harvested),0,(255,255,255))
        shadow_corn=self.font.render(str(farmer.corns_harvested),0,(0,0,0))
        
        text_energy=self.font.render(str(farmer.energy_cans),0,(255,255,255))
        shadow_energy=self.font.render(str(farmer.energy_cans),0,(0,0,0))
        
        text_money=self.big_font.render(str(farmer.money),0,(255,255,255))
        shadow_money=self.big_font.render(str(farmer.money),0,(0,0,0))

        #check if the inventory is opened
        if self.inventory_open==1:
            #if it is blit the inventory image
            screen.blit(self.image,self.rect)
            #Show money
            screen.blit(shadow_money,(29*self.TS+2,20*self.TS+1))
            screen.blit(text_money,(29*self.TS,20*self.TS))
            #check if any carrots were harvested
            if farmer.carrots_harvested>0:
                #if any where blit the carrot onto the inventory slot
                screen.blit(self.carrot,self.carrot_inventory)
                #if the amount of carrots is double digits shift the numbers
                if farmer.carrots_harvested<10:
                #blit text
                    screen.blit(shadow_carrot,(12*self.TS+9,12*self.TS+5))
                    screen.blit(text_carrot,(12*self.TS+8,12*self.TS+4))
                else:
                    screen.blit(shadow_carrot,(12*self.TS+2,12*self.TS+5))
                    screen.blit(text_carrot,(12*self.TS+1,12*self.TS+4))
                    
                if farmer.plums_harvested>0:
                    screen.blit(self.plum,self.plum_inventory2)
                    if farmer.plums_harvested<10:
                        screen.blit(shadow_plum,(12*self.TS+41,12*self.TS+5))
                        screen.blit(text_plum,(12*self.TS+40,12*self.TS+4))
                    else:
                        screen.blit(shadow_plum,(12*self.TS+34,12*self.TS+5))
                        screen.blit(text_plum,(12*self.TS+33,12*self.TS+4))
                        
                    if farmer.corns_harvested>0:
                        screen.blit(self.corn,self.corn_inventory3)
                        if farmer.corns_harvested<10:
                            screen.blit(shadow_corn,(12*self.TS+73,12*self.TS+5))
                            screen.blit(text_corn,(12*self.TS+72,12*self.TS+4))
                        else:
                            screen.blit(shadow_corn,(12*self.TS+66,12*self.TS+5))
                            screen.blit(text_corn,(12*self.TS+65,12*self.TS+4))
                        
                        if farmer.energy_cans>0:
                            screen.blit(self.energy,self.energy_inventory4)
                            self.energy_slot=4
                            if farmer.energy_cans<10:
                                screen.blit(shadow_energy,(12*self.TS+105,12*self.TS+5))
                                screen.blit(text_energy,(12*self.TS+104,12*self.TS+4))
                            else:
                                screen.blit(shadow_energy,(12*self.TS+98,12*self.TS+5))
                                screen.blit(text_energy,(12*self.TS+97,12*self.TS+4))
                    else:
                        if farmer.energy_cans>0:
                            screen.blit(self.energy,self.energy_inventory3)
                            self.energy_slot=3
                            if farmer.energy_cans<10:
                                screen.blit(shadow_energy,(12*self.TS+73,12*self.TS+5))
                                screen.blit(text_energy,(12*self.TS+72,12*self.TS+4))
                            else:
                                screen.blit(shadow_energy,(12*self.TS+66,12*self.TS+5))
                                screen.blit(text_energy,(12*self.TS+65,12*self.TS+4))
                else:
                    if farmer.corns_harvested>0:
                        screen.blit(self.corn,self.corn_inventory2)
                        if farmer.corns_harvested<10:
                            screen.blit(shadow_corn,(12*self.TS+41,12*self.TS+5))
                            screen.blit(text_corn,(12*self.TS+40,12*self.TS+4))
                        else:
                            screen.blit(shadow_corn,(12*self.TS+34,12*self.TS+5))
                            screen.blit(text_corn,(12*self.TS+33,12*self.TS+4))
                            
                        if farmer.energy_cans>0:
                            screen.blit(self.energy,self.energy_inventory3)
                            self.energy_slot=3
                            if farmer.energy_cans<10:
                                screen.blit(shadow_energy,(12*self.TS+73,12*self.TS+5))
                                screen.blit(text_energy,(12*self.TS+72,12*self.TS+4))
                            else:
                                screen.blit(shadow_energy,(12*self.TS+66,12*self.TS+5))
                                screen.blit(text_energy,(12*self.TS+65,12*self.TS+4))
                    else:
                        if farmer.energy_cans>0:
                            screen.blit(self.energy,self.energy_inventory2)
                            self.energy_slot=2
                            if farmer.energy_cans<10:
                                screen.blit(shadow_energy,(12*self.TS+41,12*self.TS+5))
                                screen.blit(text_energy,(12*self.TS+40,12*self.TS+4))
                            else:
                                screen.blit(shadow_energy,(12*self.TS+34,12*self.TS+5))
                                screen.blit(text_energy,(12*self.TS+33,12*self.TS+4))
                    
            elif farmer.carrots_harvested==0:
                if farmer.plums_harvested>0:
                    screen.blit(self.plum,self.plum_inventory1)
                    if farmer.plums_harvested<10:
                    #blit text
                        screen.blit(shadow_plum,(12*self.TS+9,12*self.TS+5))
                        screen.blit(text_plum,(12*self.TS+8,12*self.TS+4))
                    else:
                        screen.blit(shadow_plum,(12*self.TS+2,12*self.TS+5))
                        screen.blit(text_plum,(12*self.TS+1,12*self.TS+4))
                        
                    if farmer.corns_harvested>0:
                        screen.blit(self.corn,self.corn_inventory2)
                        if farmer.plums_harvested<10:
                            screen.blit(shadow_corn,(12*self.TS+41,12*self.TS+5))
                            screen.blit(text_corn,(12*self.TS+40,12*self.TS+4))
                        else:
                            screen.blit(shadow_corn,(12*self.TS+34,12*self.TS+5))
                            screen.blit(text_corn,(12*self.TS+33,12*self.TS+4))
                            
                        if farmer.energy_cans>0:
                            screen.blit(self.energy,self.energy_inventory3)
                            self.energy_slot=3
                            if farmer.energy_cans<10:
                                screen.blit(shadow_energy,(12*self.TS+73,12*self.TS+5))
                                screen.blit(text_energy,(12*self.TS+72,12*self.TS+4))
                            else:
                                screen.blit(shadow_energy,(12*self.TS+66,12*self.TS+5))
                                screen.blit(text_energy,(12*self.TS+65,12*self.TS+4))
                                
                    else:
                        if farmer.energy_cans>0:
                            screen.blit(self.energy,self.energy_inventory2)
                            self.energy_slot=2
                            if farmer.energy_cans<10:
                                screen.blit(shadow_energy,(12*self.TS+41,12*self.TS+5))
                                screen.blit(text_energy,(12*self.TS+40,12*self.TS+4))
                            else:
                                screen.blit(shadow_energy,(12*self.TS+34,12*self.TS+5))
                                screen.blit(text_energy,(12*self.TS+33,12*self.TS+4))
                        
                                
                elif farmer.corns_harvested>0:
                    screen.blit(self.corn,self.corn_inventory1)
                    if farmer.corns_harvested<10:
                        screen.blit(shadow_corn,(12*self.TS+9,12*self.TS+5))
                        screen.blit(text_corn,(12*self.TS+8,12*self.TS+4))
                    else:
                        screen.blit(shadow_corn,(12*self.TS+2,12*self.TS+5))
                        screen.blit(text_corn,(12*self.TS+1,12*self.TS+4))
                    
                    if farmer.energy_cans>0:
                        screen.blit(self.energy,self.energy_inventory2)
                        self.energy_slot=2
                        if farmer.energy_cans<10:
                            screen.blit(shadow_energy,(12*self.TS+41,12*self.TS+5))
                            screen.blit(text_energy,(12*self.TS+40,12*self.TS+4))
                        else:
                            screen.blit(shadow_energy,(12*self.TS+34,12*self.TS+5))
                            screen.blit(text_energy,(12*self.TS+33,12*self.TS+4))
                                
                else:
                    if farmer.energy_cans>0:
                        screen.blit(self.energy,self.energy_inventory1)
                        self.energy_slot=1
                        if farmer.energy_cans<10:
                            screen.blit(shadow_energy,(12*self.TS+9,12*self.TS+5))
                            screen.blit(text_energy,(12*self.TS+8,12*self.TS+4))
                        else:
                            screen.blit(shadow_energy,(12*self.TS+2,12*self.TS+5))
                            screen.blit(text_energy,(12*self.TS+1,12*self.TS+4))
            
                
            pygame.draw.rect(screen, (124,252,0), (28*self.TS-3,19*self.TS+1,farmer.stamina/100*88,6), 0)
            if farmer.energy_cans>0:
                if self.energy_info_display==1:
                    screen.blit(self.energy_info,self.energy_info1)
                    
                elif self.energy_info_display==2:
                    screen.blit(self.energy_info,self.energy_info2)
                    
                elif self.energy_info_display==3:
                    screen.blit(self.energy_info,self.energy_info3)
                    
                elif self.energy_info_display==4:
                    screen.blit(self.energy_info,self.energy_info4)
            else:
                self.energy_info_display=0
            
    def mouse(self,e,farmer):
        if farmer.energy_cans==0:
            self.energy_slot=0
        if e.type==pygame.MOUSEMOTION:
            if self.energy_slot==1:
                if self.energy_inventory1.collidepoint(e.pos):
                    self.energy_info_display=1
                else:
                    self.energy_info_display=0
                    
            if self.energy_slot==2:
                if self.energy_inventory2.collidepoint(e.pos):
                    self.energy_info_display=2
                else:
                    self.energy_info_display=0
                        
            if self.energy_slot==3:
                if self.energy_inventory3.collidepoint(e.pos):
                    self.energy_info_display=3
                else:
                    self.energy_info_display=0
                        
            if self.energy_slot==4:
                if self.energy_inventory4.collidepoint(e.pos):
                    self.energy_info_display=4
                else:
                    self.energy_info_display=0
                    
        if e.type==pygame.MOUSEBUTTONDOWN:
            if self.energy_info_display!=0:
                if farmer.stamina==100:
                    return
                else:
                    farmer.energy_cans-=1
                    if farmer.stamina+50>100:
                        farmer.stamina=100
                    else:
                        farmer.stamina+=50

class Market_UI:
    def __init__(self):
        TS=16
        x1=22.5*TS
        y1=15*TS
        self.market=pygame.image.load('market_buy_sell.png')
        self.market_rect=self.market.get_rect(center=(x1,y1))
        #make 2 rects, one for the sell button and one for the buy
        self.buy_rect=pygame.Rect(14*TS-7,14*TS-6,8*TS,3*TS)
        self.sell_rect=pygame.Rect(24*TS-11,14*TS-6,8*TS,3*TS)
        self.market_buy_open=0
        self.market_sell_open=0
        self.market_buy=pygame.image.load('market_buy.png')
        self.market_sell=pygame.image.load('market_sell.png')
        self.highlighted_box=pygame.image.load('market_buy_highlighted_slot.png')
        self.highlighted_box_sell=pygame.image.load('market_sell_highlighted_slot.png')
        self.slot_1_rect=pygame.Rect(15*TS+3,12*TS-8,4*TS,4*TS)
        self.slot_1=0
        self.slot_2_rect=pygame.Rect(20*TS+8,12*TS-8,4*TS,4*TS)
        self.slot_2=0
        self.slot_3_rect=pygame.Rect(25*TS+13,12*TS-8,4*TS,4*TS)
        self.slot_3=0
        self.slot_4_rect=pygame.Rect(15*TS+3,16*TS-1,4*TS,4*TS)
        self.slot_4=0
        self.slot_5_rect=pygame.Rect(20*TS+8,16*TS-1,4*TS,4*TS)
        self.slot_5=0
        self.slot_6_rect=pygame.Rect(25*TS+13,16*TS-1,4*TS,4*TS)
        self.slot_6=0
        #sell slots
        #row 1
        self.sell_slot_1=0
        self.sell_slot_1_rect=pygame.Rect(14*TS+2,11*TS+8,2*TS,2*TS)
        self.sell_slot_2=0
        self.sell_slot_2_rect=pygame.Rect(14*TS+32,11*TS+8,2*TS,2*TS)
        self.sell_slot_3=0
        self.sell_slot_3_rect=pygame.Rect(14*TS+61,11*TS+8,2*TS,2*TS)
        self.sell_slot_4=0
        self.sell_slot_4_rect=pygame.Rect(14*TS+91,11*TS+8,2*TS,2*TS)
        self.sell_slot_5=0
        self.sell_slot_5_rect=pygame.Rect(14*TS+120,11*TS+8,2*TS,2*TS)
        self.sell_slot_6=0
        self.sell_slot_6_rect=pygame.Rect(14*TS+149,11*TS+8,2*TS,2*TS)
        self.sell_slot_7=0
        self.sell_slot_7_rect=pygame.Rect(14*TS+179,11*TS+8,2*TS,2*TS)
        self.sell_slot_8=0
        self.sell_slot_8_rect=pygame.Rect(14*TS+208,11*TS+8,2*TS,2*TS)
        self.sell_slot_9=0
        self.sell_slot_9_rect=pygame.Rect(14*TS+238,11*TS+8,2*TS,2*TS)
        #row 2
        self.sell_slot_10=0
        self.sell_slot_10_rect=pygame.Rect(14*TS+2,11*TS+37,2*TS,2*TS)
        self.sell_slot_11=0
        self.sell_slot_11_rect=pygame.Rect(14*TS+32,11*TS+37,2*TS,2*TS)
        self.sell_slot_12=0
        self.sell_slot_12_rect=pygame.Rect(14*TS+61,11*TS+37,2*TS,2*TS)
        self.sell_slot_13=0
        self.sell_slot_13_rect=pygame.Rect(14*TS+91,11*TS+37,2*TS,2*TS)
        self.sell_slot_14=0
        self.sell_slot_14_rect=pygame.Rect(14*TS+120,11*TS+37,2*TS,2*TS)
        self.sell_slot_15=0
        self.sell_slot_15_rect=pygame.Rect(14*TS+149,11*TS+37,2*TS,2*TS)
        self.sell_slot_16=0
        self.sell_slot_16_rect=pygame.Rect(14*TS+179,11*TS+37,2*TS,2*TS)
        self.sell_slot_17=0
        self.sell_slot_17_rect=pygame.Rect(14*TS+208,11*TS+37,2*TS,2*TS)
        self.sell_slot_18=0
        self.sell_slot_18_rect=pygame.Rect(14*TS+238,11*TS+37,2*TS,2*TS)
        #row 3
        self.sell_slot_19=0
        self.sell_slot_19_rect=pygame.Rect(14*TS+2,11*TS+66,2*TS,2*TS)
        self.sell_slot_20=0
        self.sell_slot_20_rect=pygame.Rect(14*TS+32,11*TS+66,2*TS,2*TS)
        self.sell_slot_21=0
        self.sell_slot_21_rect=pygame.Rect(14*TS+61,11*TS+66,2*TS,2*TS)
        self.sell_slot_22=0
        self.sell_slot_22_rect=pygame.Rect(14*TS+91,11*TS+66,2*TS,2*TS)
        self.sell_slot_23=0
        self.sell_slot_23_rect=pygame.Rect(14*TS+120,11*TS+66,2*TS,2*TS)
        self.sell_slot_24=0
        self.sell_slot_24_rect=pygame.Rect(14*TS+149,11*TS+66,2*TS,2*TS)
        self.sell_slot_25=0
        self.sell_slot_25_rect=pygame.Rect(14*TS+179,11*TS+66,2*TS,2*TS)
        self.sell_slot_26=0
        self.sell_slot_26_rect=pygame.Rect(14*TS+208,11*TS+66,2*TS,2*TS)
        self.sell_slot_27=0
        self.sell_slot_27_rect=pygame.Rect(14*TS+238,11*TS+66,2*TS,2*TS)
        #row 4
        self.sell_slot_28=0
        self.sell_slot_28_rect=pygame.Rect(14*TS+2,11*TS+95,2*TS,2*TS)
        self.sell_slot_29=0
        self.sell_slot_29_rect=pygame.Rect(14*TS+32,11*TS+95,2*TS,2*TS)
        self.sell_slot_30=0
        self.sell_slot_30_rect=pygame.Rect(14*TS+61,11*TS+95,2*TS,2*TS)
        self.sell_slot_31=0
        self.sell_slot_31_rect=pygame.Rect(14*TS+91,11*TS+95,2*TS,2*TS)
        self.sell_slot_32=0
        self.sell_slot_32_rect=pygame.Rect(14*TS+120,11*TS+95,2*TS,2*TS)
        self.sell_slot_33=0
        self.sell_slot_33_rect=pygame.Rect(14*TS+149,11*TS+95,2*TS,2*TS)
        self.sell_slot_34=0
        self.sell_slot_34_rect=pygame.Rect(14*TS+179,11*TS+95,2*TS,2*TS)
        self.sell_slot_35=0
        self.sell_slot_35_rect=pygame.Rect(14*TS+208,11*TS+95,2*TS,2*TS)
        self.sell_slot_36=0
        self.sell_slot_36_rect=pygame.Rect(14*TS+238,11*TS+95,2*TS,2*TS)
        self.pickaxe_bought=0
        self.scythe_bought=0
        
        x1=15*TS+1
        y1=12*TS+7
        self.carrot=pygame.image.load('carrot_inventory.png')
        self.plum=pygame.image.load('plum_inventory.png')
        self.corn=pygame.image.load('corn_inventory.png')
        self.carrot_inventory=self.carrot.get_rect(center=(x1,y1))
        self.plum_inventory1=self.plum.get_rect(center=(x1,y1))
        self.plum_inventory2=self.plum.get_rect(center=(x1+30,y1))
        self.corn_inventory1=self.plum.get_rect(center=(x1,y1))
        self.corn_inventory2=self.plum.get_rect(center=(x1+30,y1))
        self.corn_inventory3=self.plum.get_rect(center=(x1+59,y1))
        
        self.gold_image=pygame.image.load('gold.png')
        self.gold_image_rect=self.gold_image.get_rect(center=(17*TS+231,14*TS+90))
        
        pygame.font.init()
        self.font=pygame.font.SysFont('consolas',12,bold=1)
        self.big_font=pygame.font.SysFont('consolas',20)
    def mouse(self,e,farmer):
        #get the most position
        if e.type==pygame.MOUSEMOTION:
            #depending where the mouse is change the picture so that the selected button is highlighted
            if self.buy_rect.collidepoint(e.pos):
                self.market=pygame.image.load('market_buy_highlighted.png')
            elif self.sell_rect.collidepoint(e.pos):
                self.market=pygame.image.load('market_sell_highlighted.png')
            else:
                self.market=pygame.image.load('market_buy_sell.png')
            #buy market slots
            if self.market_buy_open==1:
                if self.slot_1_rect.collidepoint(e.pos):
                    self.slot_1=1
                else:
                    self.slot_1=0
                    
                if self.slot_2_rect.collidepoint(e.pos):
                    self.slot_2=1
                else:
                    self.slot_2=0
                    
                if self.slot_3_rect.collidepoint(e.pos):
                    self.slot_3=1
                else:
                    self.slot_3=0
                    
                if self.slot_4_rect.collidepoint(e.pos):
                    self.slot_4=1
                else:
                    self.slot_4=0
                    
                if self.slot_5_rect.collidepoint(e.pos):
                    self.slot_5=1
                else:
                    self.slot_5=0
                    
                if self.slot_6_rect.collidepoint(e.pos):
                    self.slot_6=1
                else:
                    self.slot_6=0
                    
            elif self.market_sell_open==1:
                if self.sell_slot_1_rect.collidepoint(e.pos):
                    self.sell_slot_1=1
                else:
                    self.sell_slot_1=0
                    
                if self.sell_slot_2_rect.collidepoint(e.pos):
                    self.sell_slot_2=1
                else:
                    self.sell_slot_2=0
                if self.sell_slot_3_rect.collidepoint(e.pos):
                    self.sell_slot_3=1
                else:
                    self.sell_slot_3=0
                    
                if self.sell_slot_4_rect.collidepoint(e.pos):
                    self.sell_slot_4=1
                else:
                    self.sell_slot_4=0
                if self.sell_slot_5_rect.collidepoint(e.pos):
                    self.sell_slot_5=1
                else:
                    self.sell_slot_5=0
                    
                if self.sell_slot_6_rect.collidepoint(e.pos):
                    self.sell_slot_6=1
                else:
                    self.sell_slot_6=0
                if self.sell_slot_7_rect.collidepoint(e.pos):
                    self.sell_slot_7=1
                else:
                    self.sell_slot_7=0
                    
                if self.sell_slot_8_rect.collidepoint(e.pos):
                    self.sell_slot_8=1
                else:
                    self.sell_slot_8=0
                if self.sell_slot_9_rect.collidepoint(e.pos):
                    self.sell_slot_9=1
                else:
                    self.sell_slot_9=0
               
                if self.sell_slot_10_rect.collidepoint(e.pos):
                    self.sell_slot_10=1
                else:
                    self.sell_slot_10=0
                    
                if self.sell_slot_11_rect.collidepoint(e.pos):
                    self.sell_slot_11=1
                else:
                    self.sell_slot_11=0
                if self.sell_slot_12_rect.collidepoint(e.pos):
                    self.sell_slot_12=1
                else:
                    self.sell_slot_12=0
                    
                if self.sell_slot_13_rect.collidepoint(e.pos):
                    self.sell_slot_13=1
                else:
                    self.sell_slot_13=0
                if self.sell_slot_14_rect.collidepoint(e.pos):
                    self.sell_slot_14=1
                else:
                    self.sell_slot_14=0
                    
                if self.sell_slot_15_rect.collidepoint(e.pos):
                    self.sell_slot_15=1
                else:
                    self.sell_slot_15=0
                if self.sell_slot_16_rect.collidepoint(e.pos):
                    self.sell_slot_16=1
                else:
                    self.sell_slot_16=0
                    
                if self.sell_slot_17_rect.collidepoint(e.pos):
                    self.sell_slot_17=1
                else:
                    self.sell_slot_17=0
                if self.sell_slot_18_rect.collidepoint(e.pos):
                    self.sell_slot_18=1
                else:
                    self.sell_slot_18=0
                if self.sell_slot_19_rect.collidepoint(e.pos):
                    self.sell_slot_19=1
                else:
                    self.sell_slot_19=0
                    
                if self.sell_slot_20_rect.collidepoint(e.pos):
                    self.sell_slot_20=1
                else:
                    self.sell_slot_20=0
                if self.sell_slot_21_rect.collidepoint(e.pos):
                    self.sell_slot_21=1
                else:
                    self.sell_slot_21=0
                    
                if self.sell_slot_22_rect.collidepoint(e.pos):
                    self.sell_slot_22=1
                else:
                    self.sell_slot_22=0
                if self.sell_slot_23_rect.collidepoint(e.pos):
                    self.sell_slot_23=1
                else:
                    self.sell_slot_23=0
                    
                if self.sell_slot_24_rect.collidepoint(e.pos):
                    self.sell_slot_24=1
                else:
                    self.sell_slot_24=0
                if self.sell_slot_25_rect.collidepoint(e.pos):
                    self.sell_slot_25=1
                else:
                    self.sell_slot_25=0
                    
                if self.sell_slot_26_rect.collidepoint(e.pos):
                    self.sell_slot_26=1
                else:
                    self.sell_slot_26=0
                if self.sell_slot_27_rect.collidepoint(e.pos):
                    self.sell_slot_27=1
                else:
                    self.sell_slot_27=0
               
                if self.sell_slot_28_rect.collidepoint(e.pos):
                    self.sell_slot_28=1
                else:
                    self.sell_slot_28=0
                    
                if self.sell_slot_29_rect.collidepoint(e.pos):
                    self.sell_slot_29=1
                else:
                    self.sell_slot_29=0
                if self.sell_slot_30_rect.collidepoint(e.pos):
                    self.sell_slot_30=1
                else:
                    self.sell_slot_30=0
                    
                if self.sell_slot_31_rect.collidepoint(e.pos):
                    self.sell_slot_31=1
                else:
                    self.sell_slot_31=0
                if self.sell_slot_32_rect.collidepoint(e.pos):
                    self.sell_slot_32=1
                else:
                    self.sell_slot_32=0
                    
                if self.sell_slot_33_rect.collidepoint(e.pos):
                    self.sell_slot_33=1
                else:
                    self.sell_slot_33=0
                if self.sell_slot_34_rect.collidepoint(e.pos):
                    self.sell_slot_34=1
                else:
                    self.sell_slot_34=0
                    
                if self.sell_slot_35_rect.collidepoint(e.pos):
                    self.sell_slot_35=1
                else:
                    self.sell_slot_35=0
                if self.sell_slot_36_rect.collidepoint(e.pos):
                    self.sell_slot_36=1
                else:
                    self.sell_slot_36=0
        #if the buy or sell button is clicked then open up their menus
        if e.type==pygame.MOUSEBUTTONDOWN:
            if self.market_buy_open==0 and self.market_sell_open==0:
                if self.buy_rect.collidepoint(e.pos):
                    self.market_buy_open=1
                elif self.sell_rect.collidepoint(e.pos):
                    self.market_sell_open=1
            elif self.market_buy_open==1:
                if self.slot_1_rect.collidepoint(e.pos):
                    if self.pickaxe_bought==0 and farmer.money>=10:
                        farmer.money-=10
                        self.pickaxe_bought=1
                    #add pickaxe to inventory
                    #make it so pickaxe can only be bought once
                if self.slot_2_rect.collidepoint(e.pos):
                    if self.scythe_bought==0 and farmer.money>=10:
                        farmer.money-=10
                        self.scythe_bought=1 
                if self.slot_3_rect.collidepoint(e.pos):
                    if farmer.money>0:
                        if farmer.carrot_seed<99:
                            farmer.money-=1
                            farmer.carrot_seed+=1
                if self.slot_4_rect.collidepoint(e.pos):
                    if farmer.money>2:
                        if farmer.plum_seed<99:
                            farmer.money-=3
                            farmer.plum_seed+=1
                            
                if self.slot_5_rect.collidepoint(e.pos):
                    if farmer.money>4:
                        if farmer.corn_seed<99:
                            farmer.money-=5
                            farmer.corn_seed+=1
                            
                if self.slot_6_rect.collidepoint(e.pos):
                    if farmer.money>4:
                        if farmer.energy_cans<99:
                            farmer.money-=5
                            farmer.energy_cans+=1
                            
            elif self.market_sell_open==1:
                if self.sell_slot_1_rect.collidepoint(e.pos):
                    if farmer.carrots_harvested>0:
                        farmer.carrots_harvested-=1
                        farmer.money+=5
                    elif farmer.plums_harvested>0:
                        farmer.plums_harvested-=1
                        farmer.money+=15
                    elif farmer.corns_harvested>0:
                        farmer.corns_harvested-=1
                        farmer.money+=30
                elif self.sell_slot_2_rect.collidepoint(e.pos):
                    if farmer.plums_harvested>0:
                        farmer.plums_harvested-=1
                        farmer.money+=15
                    elif farmer.corns_harvested>0:
                        farmer.corns_harvested-=1
                        farmer.money+=30
                elif self.sell_slot_3_rect.collidepoint(e.pos):
                    if farmer.corns_harvested>0:
                        farmer.corns_harvested-=1
                        farmer.money+=30
    def draw(self,screen,farmer,inventory):
        farmer_thousands=round((farmer.money/1000),1)
        TS=16
        text_carrot=self.font.render(str(farmer.carrots_harvested),0,(255,255,255))
        shadow_carrot=self.font.render(str(farmer.carrots_harvested),0,(0,0,0))
        
        text_plum=self.font.render(str(farmer.plums_harvested),0,(255,255,255))
        shadow_plum=self.font.render(str(farmer.plums_harvested),0,(0,0,0))
        
        text_corn=self.font.render(str(farmer.corns_harvested),0,(255,255,255))
        shadow_corn=self.font.render(str(farmer.corns_harvested),0,(0,0,0))
        
        text_money=self.big_font.render(str(farmer.money),0,(255,255,255))
        shadow_money=self.big_font.render(str(farmer.money),0,(0,0,0))
        
        text_money_thousands=self.big_font.render(str(farmer_thousands)+'K',0,(255,255,255))
        shadow_money_thousands=self.big_font.render(str(farmer_thousands)+'K',0,(0,0,0))
         #if the market is closed then set sell and buy open to false 
        if farmer.market_open==0:
            self.market_buy_open=0
            self.market_sell_open=0
        if farmer.market_open==1:
            inventory.inventory_open=0
            screen.blit(self.market,self.market_rect)
            if self.market_buy_open==1:
                screen.blit(self.market_buy,self.market_rect)
            elif self.market_sell_open==1:
                screen.blit(self.market_sell,self.market_rect)
        if self.market_buy_open==1:
            if self.slot_1==1:
                screen.blit(self.highlighted_box,self.slot_1_rect)
            if self.slot_2==1:
                screen.blit(self.highlighted_box,self.slot_2_rect)
            if self.slot_3==1:
                screen.blit(self.highlighted_box,self.slot_3_rect)
            if self.slot_4==1:
                screen.blit(self.highlighted_box,self.slot_4_rect)
            if self.slot_5==1:
                screen.blit(self.highlighted_box,self.slot_5_rect)
            if self.slot_6==1:
                screen.blit(self.highlighted_box,self.slot_6_rect)
                
        elif self.market_sell_open==1:
            
            if farmer.carrots_harvested>0:
                screen.blit(self.carrot,self.carrot_inventory)
                if farmer.carrots_harvested<10:
                    screen.blit(shadow_carrot,(15*TS+7,12*TS+9))
                    screen.blit(text_carrot,(15*TS+6,12*TS+8))
                else:
                    screen.blit(shadow_carrot,(15*TS,12*TS+9))
                    screen.blit(text_carrot,(15*TS-1,12*TS+8))
                    
                if farmer.plums_harvested>0:
                    screen.blit(self.plum,self.plum_inventory2)
                    if farmer.plums_harvested<10:
                        screen.blit(shadow_plum,(15*TS+37,12*TS+9))
                        screen.blit(text_plum,(15*TS+36,12*TS+8))
                    else:
                        screen.blit(shadow_plum,(15*TS+30,12*TS+9))
                        screen.blit(text_plum,(15*TS+29,12*TS+8))
                    if farmer.corns_harvested>0:
                        screen.blit(self.corn,self.corn_inventory3)
                        if farmer.corns_harvested<10:
                            screen.blit(shadow_corn,(15*TS+66,12*TS+9))
                            screen.blit(text_corn,(15*TS+65,12*TS+8))
                        else:
                            screen.blit(shadow_corn,(15*TS+59,12*TS+9))
                            screen.blit(text_corn,(15*TS+58,12*TS+8))
                else:
                    if farmer.corns_harvested>0:
                        screen.blit(self.corn,self.corn_inventory2)
                        if farmer.plums_harvested<10:
                            screen.blit(shadow_corn,(15*TS+37,12*TS+9))
                            screen.blit(text_corn,(15*TS+36,12*TS+8))
                        else:
                            screen.blit(shadow_corn,(15*TS+30,12*TS+9))
                            screen.blit(text_corn,(15*TS+29,12*TS+8))
            elif farmer.carrots_harvested==0:
                if farmer.plums_harvested>0:
                    screen.blit(self.plum,self.plum_inventory1)
                    if farmer.plums_harvested<10:
                        screen.blit(shadow_plum,(15*TS+7,12*TS+9))
                        screen.blit(text_plum,(15*TS+6,12*TS+8))
                    else:
                        screen.blit(shadow_plum,(15*TS,12*TS+9))
                        screen.blit(text_plum,(15*TS-1,12*TS+8))
                    if farmer.corns_harvested>0:
                        screen.blit(self.corn,self.corn_inventory2)
                        if farmer.plums_harvested<10:
                            screen.blit(shadow_corn,(15*TS+37,12*TS+9))
                            screen.blit(text_corn,(15*TS+36,12*TS+8))
                        else:
                            screen.blit(shadow_corn,(15*TS+30,12*TS+9))
                            screen.blit(text_corn,(15*TS+29,12*TS+8))
                else:
                    if farmer.corns_harvested>0:
                        screen.blit(self.corn,self.corn_inventory1)
                        if farmer.plums_harvested<10:
                            screen.blit(shadow_corn,(15*TS+7,12*TS+9))
                            screen.blit(text_corn,(15*TS+6,12*TS+8))
                        else:
                            screen.blit(shadow_corn,(15*TS,12*TS+9))
                            screen.blit(text_corn,(15*TS-1,12*TS+8))
                
            if self.sell_slot_1==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_1_rect)
            if self.sell_slot_2==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_2_rect)
            if self.sell_slot_3==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_3_rect)
            if self.sell_slot_4==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_4_rect)
            if self.sell_slot_5==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_5_rect)
            if self.sell_slot_6==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_6_rect)
            if self.sell_slot_7==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_7_rect)
            if self.sell_slot_8==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_8_rect)
            if self.sell_slot_9==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_9_rect)
            if self.sell_slot_10==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_10_rect)
            if self.sell_slot_11==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_11_rect)
            if self.sell_slot_12==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_12_rect)
            if self.sell_slot_13==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_13_rect)
            if self.sell_slot_14==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_14_rect)
            if self.sell_slot_15==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_15_rect)
            if self.sell_slot_16==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_16_rect)
            if self.sell_slot_17==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_17_rect)
            if self.sell_slot_18==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_18_rect)
            if self.sell_slot_19==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_19_rect)
            if self.sell_slot_20==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_20_rect)
            if self.sell_slot_21==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_21_rect)
            if self.sell_slot_22==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_22_rect)
            if self.sell_slot_23==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_23_rect)
            if self.sell_slot_24==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_24_rect)
            if self.sell_slot_25==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_25_rect)
            if self.sell_slot_26==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_26_rect)
            if self.sell_slot_27==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_27_rect)
            if self.sell_slot_28==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_28_rect)
            if self.sell_slot_29==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_29_rect)
            if self.sell_slot_30==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_30_rect)
            if self.sell_slot_31==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_31_rect)
            if self.sell_slot_32==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_32_rect)
            if self.sell_slot_33==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_33_rect)
            if self.sell_slot_34==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_34_rect)
            if self.sell_slot_35==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_35_rect)
            if self.sell_slot_36==1:
                screen.blit(self.highlighted_box_sell,self.sell_slot_36_rect)
        if self.market_buy_open==1 or self.market_sell_open==1:
            screen.blit(self.gold_image,self.gold_image_rect)
            if farmer.money<1000:
                screen.blit(shadow_money,(31*TS+2,19*TS))
                screen.blit(text_money,(31*TS,19*TS-1))
            else:
                screen.blit(shadow_money_thousands,(31*TS+2,19*TS))
                screen.blit(text_money_thousands,(31*TS,19*TS-1))
                
