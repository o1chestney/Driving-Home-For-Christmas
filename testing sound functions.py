#i made this file to test the functions, the bottom row of keys are binded to running the functions

#keybinds:
#z - point()
#x - hit()
#c - loose()
#v - pause()
#b - unpause()

#Making the window
import pygame
pygame.init()

#defining sounds
crash = pygame.mixer.Sound('crash.wav')
present = pygame.mixer.Sound('present_gain.wav')

#player gains a point
def point():
    pygame.mixer.Sound.play(present)
    present.set_volume(0.6)

#player looses a life
def hit():
    pygame.mixer.Sound.play(crash)
    crash.set_volume(0.8)

#player looses the game
def loose():
    pygame.mixer.Sound.play(crash)
    crash.set_volume(0.8)
    pygame.mixer.music.stop()

#game paused
def pause():
    pygame.mixer.music.pause()

#game unpaused
def unpause():
    pygame.mixer.music.unpause()

#starts music loop
def music():
    pygame.mixer.music.load('music.wav')
    pygame.mixer.music.play(-1)

music()

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
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_a] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
    if keys[pygame.K_d] and x < 500 - vel - width:
        x += vel

    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_w] and y > vel:
        y -= vel

    if keys[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel  
    if keys[pygame.K_s] and y < 500 - height - vel:
        y += vel

    #testing functions, remove later
    if keys[pygame.K_z]:
        point()
    if keys[pygame.K_x]:
        hit()
    if keys[pygame.K_c]:
        loose()
    if keys[pygame.K_v]:
        pause()
    if keys[pygame.K_b]:
        unpause()
                 
    win.fill((0,0,0))
    #drawing the character
    pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    pygame.display.update()

pygame.quit()