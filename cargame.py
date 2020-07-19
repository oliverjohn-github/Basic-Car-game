import pygame
import time
import random
import os

pygame.init()

crash_sound = pygame.mixer.Sound("sounds/crashsound.wav")

best_score = 0
maxi=[]
display_width=800
display_height=600

black=(0,0,0)
white=(255,255,255)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
block_color= (53,115,255)

car_width = 73
pause = False
leveled = False

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('my game')
clock=pygame.time.Clock()

carImg =pygame.image.load(os.path.join("images","racecar.png"))
Gamelogo = pygame.image.load(os.path.join("images","startgamelogo.png"))
Gametitle = pygame.image.load(os.path.join("images","gametitle.png"))


def button(msg,x,y,w,h,ic,ac,action = None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x+w and y < mouse[1] < y+h: 
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    action == None

        if click[0] == 1 and action != None:
            action()
            
                    
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))


    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf ,textRect = text_objects(msg, smallText)
    textRect.center= ( (x+(w/2)),(y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
    

def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def target(increase):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("target: " +str(increase), True, black)
    gameDisplay.blit(text,(675,0))

def highscore(top):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("best: " +str(top), True, black)
    gameDisplay.blit(text,((400/2),(300/2)))

def yourscore(crashscore):
    global score
    font = pygame.font.SysFont("comicsansms", 45)
    text = font.render("Yourscore: " +str(crashscore), True, black)
    gameDisplay.blit(text,((600/2),(400/2)))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color,[thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text ,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont("comicsansms",75)
    TextSurf ,TextRect = text_objects(text, largeText)
    TextRect.center= ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash(your_score,top_score):
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    largeText = pygame.font.SysFont("comicsansms",75)
    TextSurf ,TextRect = text_objects("Oops you crashed", largeText)
    TextRect.center= ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    yourscore(your_score)
    highscore(top_score)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)
        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("QUIT!",550,450,100,50, red,bright_red,quitgame)



        
        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():
    pygame.mixer.music.pause()
    largeText = pygame.font.SysFont("comicsansms",75)
    TextSurf ,TextRect = text_objects("Game paused", largeText)
    TextRect.center= ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
   

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)
        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("QUIT!",550,450,100,50, red,bright_red,quitgame)



        
        pygame.display.update()
        clock.tick(15)

def nextlevel():
    global leveled
    pygame.mixer.music.unpause()
    leveled = False

def level(levelno):
    pygame.mixer.music.pause()
    largeText = pygame.font.SysFont("comicsansms",75)
    TextSurf ,TextRect = text_objects("Level - "+str(levelno), largeText)
    TextRect.center= ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
   

    while leveled:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Continue",150,450,100,50,green,bright_green,nextlevel)
        button("QUIT!",550,450,100,50, red,bright_red,quitgame)

        #gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(15)

def instructions():
    pygame.mixer.music.pause()
    largeText = pygame.font.SysFont("comicsansms",30)
    TextSurf ,TextRect = text_objects("INSTRUCTIONS: ", largeText)
    TextRect.center= (220,100)
    font = pygame.font.SysFont("comicsansms", 20)
    text1 = font.render("1.Keeping dodging the blocks by pressing left and right keys " , True, black)
    text2 = font.render("2.Reach target to go to next level" , True, black)
    text3 = font.render("3.Press 'P' to pause" , True, black)
    gameDisplay.fill(white)
    gameDisplay.blit(text1,(150,150))
    gameDisplay.blit(text2,(150,200))
    gameDisplay.blit(text3,(150,250))
    gameDisplay.blit(TextSurf ,TextRect )
   
 
    while  True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("<= BACK",350,450,100,50,green,bright_green,game_intro)
##        button("START",150,450,100,50,green,bright_green,game_loop)
##       button("QUIT!",550,450,100,50, red,bright_red,quitgame)

        #gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(15)

    
    
def game_intro():
    
    
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
##        largeText = pygame.font.SysFont("comicsansms",75)
##        TextSurf ,TextRect = text_objects("Dodge racer", largeText)
##        TextRect.center= ((display_width/2),(display_height/2))
##        gameDisplay.blit(TextSurf, TextRect)

        button("READY !",150,450,100,50,green,bright_green,game_loop)
        button("QUIT!",550,450,100,50, red,bright_red,quitgame)
        button("Game info",75,520,100,50,green,bright_green,instructions)
        c=(display_width*0.2)
        d=(display_height*0.2)
        gameDisplay.blit(Gametitle,(c,d))
        a=(display_width*0.4)
        b=(display_height*0.8)
        gameDisplay.blit(Gamelogo,(a,b))
        
        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    global leveled
    global best_score
    global maxi
    pygame.mixer.music.load("sounds/track01.wav")
    pygame.mixer.music.play(-1)
    x=(display_width*0.45)
    y=(display_height*0.8)
    score =0
    x_change=0

      #box dim
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    thingCount = 1
    blocksize = 50
    dodged = 0
    n=10
    difficulty = 1
    gameExit=False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #pressing the cross exit game
                quit()

            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change=-15
                if event.key == pygame.K_RIGHT:
                    x_change=15
                if event.key ==  pygame.K_p:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0
            


        x += x_change        
        gameDisplay.fill(white)
        
        
        #box blocking the way function call
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x,y) #displaying car
        target(n)
        things_dodged(dodged)
        

        if x > display_width - car_width or x < 0:
            crash(score,best_score)#when car crashes

        if thing_starty > display_height:
            thing_width = 100
            thing_starty = 0 - thing_height #displays block when it goes off the screen
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            score = dodged
            maxi.append(score)
            thing_width += random.randrange(0, blocksize * 3)#(blocksize, blocksize * 2)#(dodged*1.05)
            thing_speed += 0.2

            if dodged - 1  == n :
                x=(display_width*0.45)
                y=(display_height*0.8)
                thing_speed = 7
                thing_width = 100
                thing_starty = -600
                dodged = 0
                difficulty = difficulty + 1
                leveled = True
                level(difficulty)
                n+=10
                
            
            best_score=max(maxi)
                
                
            #thing_speed += 1
            #thing_width += (dodged*1.2)

#if the car bumps into any of the boxes
        if y < thing_starty + thing_height:

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash(score,best_score)
##        if dodged  == n :
##            difficulty = difficulty + 1
##            leveled = True
##            level(difficulty)
##            dodged = 0
##            n+=5
##            
##            thing_width += (dodged*1.2)
          
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()
