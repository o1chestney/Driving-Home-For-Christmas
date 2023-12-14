import pygame


#add this code at any point before the game is ran in main.py
#i didnt add it myself because i dont know what version is the latest one and i dont want to break anything

#i can add these functions to existing functions if they have the same purpose just let me know where theyre needed
#the music sounds low quality because github wont let me upload the uncompressed version but i have it if we need it

#required for the file to run
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

#calls the music to be started
music()