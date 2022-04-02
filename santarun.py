import pygame
import random
import sys
import time
from pygame.locals import * #

from pygame.constants import KEYDOWN, K_ESCAPE, K_SPACE, K_UP, QUIT


# setting screen size
screen_width=800
screen_height=424
WHITE=(250,250,250)
ground_y=screen_height*0.8
SCREEN=pygame.display.set_mode((screen_width,screen_height))
FPS=32
FPSCLOCK=pygame.time.Clock() 
basex=0
WHITE=(250,250,250)
#rgb values
white = (255,255,255)
green = (0,255,0)
blue = (0,0,128)
treex=600
player_x=50
player_y=320
background_x=0
jump=False
background_y=0
tree1_y=300
tree2_y=290
tree3_y=320
background_image=(pygame.image.load('background.png').convert())
game_sprites={}


def snow_fall():
    snowfall=[]
    for i in range(5):
                    x=random.randrange(0,800)
                    y=random.randrange(0,424)
                    snowfall.append([x,y])
                    global background_x
                    background_x -=5
                    draw_bg()


                    for i in range(len(snowfall)):
                        # Draw the snow flake  
                            pygame.draw.circle(SCREEN, WHITE, snowfall[i], 3)
                    
                            # Move the snow flake down one pixel
                            snowfall[i][1] += 1
                    
                            # If the snow flake has moved off the bottom of the screen
                            if snowfall[i][1] > 424:
                                # Reset it just above the top
                                y = random.randrange(-5, 0)
                                snowfall[i][1] = y
                                # Give it a new x position
                                x = random.randrange(0, 800)
                                snowfall[i][0] =x







def draw_base():
    global basex
    SCREEN.blit(game_sprites['base'],(basex,370))
    SCREEN.blit(game_sprites['base'],(basex+800,370))
    if basex <= -800:
        basex=0

def draw_bg():
    global background_x
    SCREEN.blit(background_image,(background_x,background_y))
    SCREEN.blit(background_image,(background_x+800,background_y))
    if(background_x==-800):
        background_x=0

def get_tree():
    
     global treex
     SCREEN.blit(game_sprites['tree1'],(treex,tree1_y))
     SCREEN.blit(game_sprites['tree2'],(treex+600,tree2_y))
     SCREEN.blit(game_sprites['tree3'],(treex+1100,tree3_y))

     if treex ==-1300:
         treex=400
        



     
    

def welcome_Screen():
   
    while(True):
        for event in pygame.event.get():
            # if close button is clicked close the game
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()

            # if user press space key or button up start the game
            if event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                return

            
        snow_fall()
        global basex
        basex -=10
        draw_base()
        # SCREEN.blit(game_sprites['player'],bird_rect)
        SCREEN.blit(game_sprites['tree3'],(400,320))
        SCREEN.blit(game_sprites['player'],(200,320))
        SCREEN.blit(game_sprites['tree2'],(600,290))    
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def main_game():
        score=0
        base_x=0
        global FPSCLOCK
        global treex,game
        global player_x,player_y,jump

        while(True): 
            global jump,player_y
            for event in pygame.event.get():
                # if close button is clicked close the game
                if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                if event.type==KEYDOWN and  (event.key==K_UP or event.type==K_SPACE): 
                    if player_y==320:
                        jump=True
            if 200<player_y<=320:
                    if jump==True:
                        player_y-=20
            else:
                    jump=False

            if player_y<320:
                    if jump==False:
                        player_y+=20


                    
                     

            snow_fall()
            global basex
            basex -=10
            draw_base()
            global treex
            treex -=20
            get_tree()
            SCREEN.blit(game_sprites['player'],(player_x,player_y))
            if treex<player_x+game_sprites['player'].get_width()<treex+60 and  tree1_y<=player_y+game_sprites['player'].get_height()<=tree1_y+game_sprites['tree1'].get_height():
                font = pygame.font.Font('Decay-M5RB.ttf',34)
                text_surface= font.render('GAME OVER',True,blue)
                SCREEN.fill(white)
                SCREEN.blit(text_surface,(screen_width/3,screen_height/2))
                time.sleep(0.8)
                treex=400
                player_x=50
                player_y=320
                jump=False
            if treex+620<player_x+game_sprites['player'].get_width()<treex+600+60 and tree2_y<=player_y+game_sprites['player'].get_height()<=tree2_y+game_sprites['tree2'].get_height():
                font = pygame.font.Font('Decay-M5RB.ttf',34)
                text_surface= font.render('GAME OVER',True,blue)
                SCREEN.fill(white)
                SCREEN.blit(text_surface,(screen_width/3,screen_height/2))
                time.sleep(0.8)
                treex=400
                player_x=50
                player_y=320
                jump=False
            if treex+1100<player_x+game_sprites['player'].get_width()<treex+1100+60 and tree3_y<=player_y+game_sprites['player'].get_height()<=tree3_y+game_sprites['tree3'].get_height():
                font = pygame.font.Font('Decay-M5RB.ttf',34)
                text_surface= font.render('GAME OVER',True,blue)
                SCREEN.fill(white)
                SCREEN.blit(text_surface,(screen_width/3,screen_height/2))
                time.sleep(0.8)
                treex=400
                player_x=50
                player_y=320
                jump=False
            FPSCLOCK.tick(10)        
            pygame.display.update()
           

      
if __name__=="__main__":
    # Initialize the game engine
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption("GAME")
    game_sprites['player']=(pygame.image.load('bird.png').convert())
    game_sprites['base']=(pygame.image.load('base.png').convert())
    game_sprites['tree1']=pygame.image.load('tree1.png').convert()
    game_sprites['tree2']=pygame.image.load('tree2.png').convert()
    game_sprites['tree3']=pygame.image.load('tree3.png').convert()
   
        
   
   
    


    while True:
        welcome_Screen()
        main_game()





    

