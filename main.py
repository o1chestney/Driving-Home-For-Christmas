#Making the window
import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Driving home for Christmas")

#Setting up movement variables
x = 50
y = 50
width = 50
height = 50
vel = 10

#step 7
isJump = False
jumpCount = 10

#Creating a main loop
run = True

while run:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #Event checking, so keys make the character move
    #setting the boudries (Goes after the keys[pygame.....] and (here))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and x < 500 - vel - width:
        x += vel
    if keys[pygame.K_UP] or keys[pygame.K_w] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] or keys[pygame.K_s] and y < 500 - height - vel:
        y += vel  
            
                  
    win.fill((0,0,0))
    #drawing the character
    pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    pygame.display.update()

pygame.quit()