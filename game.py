import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as fps

pygame.init()
##veriables
ww = 400
wh = 900
refresh = 30
time = fps.Clock()
player = pygame.Rect( 160, 835, 50,50)
x_speed = 8
y_speed = 3
y_speed1 = 3
y_speed2 = 3
y_speed3 = 3
y_speed4 = 3
carrot = pygame.Rect(random.randrange(ww),0,10,20)
carrot1 = pygame.Rect(random.randrange(ww),0,10,20)
carrot2 = pygame.Rect(random.randrange(ww),0,10,20)
carrot3 = pygame.Rect(random.randrange(ww),0,10,20)
carrot4 = pygame.Rect(random.randrange(ww),0,10,20)
chicken = pygame.Rect(3,50,34,47)
score = 0
roll = 0
flycount = 0

window = pygame.display.set_mode((ww,wh))
pygame.display.set_caption("AVOID THE CARROTS")
barrelmonkey = pygame.image.load("background.png")
carrotg = pygame.image.load("carrot.png")
background = pygame.image.load("background.png")
chickenfly = pygame.image.load("chicken1.png")


running = True

leftROLL = False
rightROLL = False
hit = False
chickenflys = True

def flychicken():
    global chickenflys
    
    
    
    if chickenflys is True:
        if chicken.x > 0 and chicken.x -5 > 0 :
            chicken.x -= 3
        elif chicken.x > 0 and chicken.x -5 < 0:
            chickenflys = False
            
    if chickenflys is False:
        if chicken.x + chicken.width < ww and (chicken.x + chicken.width) + 5 < ww:
            chicken.x += 3
        elif chicken.x + chicken.width < ww and (chicken.x + chicken.width) + 5 > ww:
            chickenflys = True
        

def monkeybarrel():
    global y_speed, y_speed1, y_speed2, y_speed3, y_speed4, roll

    
    if leftROLL is True:
        if player.x > 0 and player.x -5 > 0:
            player.x -= 5
            roll += 5
        elif player.x > 0 and player.x -5 < 0:
            player.x = 0
            
    if rightROLL is True:
        if player.x + player.width < ww and (player.x + player.width) + 5 < ww:
            player.x += 5
            roll -= 5
        elif player.x + player.width < ww and (player.x + player.width) + 5 > ww:
            player.x = ww - player.width
            
    if player.colliderect(carrot) or player.colliderect(carrot1) or player.colliderect(carrot2) or player.colliderect(carrot3) or player.colliderect(carrot4):
        y_speed = 0
        y_speed1 = 0
        y_speed2 = 0
        y_speed3 = 0
        y_speed4 = 0
        carrot.y = player.y
        carrot.width = ww
        carrot.x = 0
        window.blit(text, (ww/2, wh/2))
        window.blit(lose, (150,500))

            
        
            
def carrotfall():
    global y_speed, y_speed1, y_speed2,y_speed3,y_speed4, score
    
    carrot.y += y_speed
    if carrot.y >= wh:
        carrot.y = chicken.y
        carrot.x = chicken.x
        y_speed = random.randrange(5,10)
        score += 1
        
    carrot1.y += y_speed1
    if carrot1.y >= wh:
        carrot1.y = chicken.y
        carrot1.x = chicken.x
        y_speed1 = random.randrange(5, 10)
        score += 1
        
    carrot2.y += y_speed2
    if carrot2.y >= wh:
        carrot2.y = chicken.y
        carrot2.x = chicken.x
        y_speed2 = random.randrange(5, 10)
        score += 1
        
    carrot3.y += y_speed3
    if carrot3.y >= wh:
        carrot3.y = chicken.y
        carrot3.x = chicken.x
        y_speed3 = random.randrange(5,10)
        score += 1
        
    carrot4.y += y_speed4
    if carrot4.y >= wh:
        carrot4.y = chicken.y
        carrot4.x = chicken.x
        y_speed4 = random.randrange(5,10)
        score += 1

while True:

    
        
     
        window.fill((0,0,0))
        window.blit(background,(0,0))
     
        window.blit(pygame.transform.rotate(barrelmonkey, roll), player)
        window.blit(carrotg, carrot)
        window.blit(carrotg, carrot1)
        window.blit(carrotg, carrot2)
        window.blit(carrotg, carrot3)
        window.blit(carrotg, carrot4)
        window.blit(chickenfly, chicken)
        
     
        monkeybarrel()
        carrotfall()
        flychicken()
     
        font = pygame.font.Font(None,74)
        text = font.render(str(score), 1, (255,255,255))
        window.blit(text,(3,0))
        font = pygame.font.Font(None,74)
        lose = font.render(str("ya lose"), 1, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
     
        for event in GAME_EVENTS.get():
         
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leftROLL = True
                if event.key == pygame.K_RIGHT:
                    rightROLL = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    leftROLL = False
                if event.key == pygame.K_RIGHT:
                    rightROLL = False
        
            if event.type == GAME_GLOBALS.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        time.tick(refresh)
    
     
