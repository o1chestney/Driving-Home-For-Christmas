#i made this file to test the functions, the bottom row of keys are binded to running the functions
#this is an updated version to work with the most recent version of main2.py. still only for testing

#keybinds:
#z - point()
#x - hit()
#c - loose()
#v - pause()
#b - unpause()

# Importing ---------------
import pygame, sys
pygame.init()
from config import *
from sprites import *
from asset_loader import *

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

# Running the game --------------------------------------------------------
class Game:
    def __init__(self):
        self.running = True

        self.screen = pygame.display.set_mode((WIN_WIDTH, # Setting the screen size
                                              WIN_WIDTH), pygame.FULLSCREEN) # to fit the user's screen
        self.clock=pygame.time.Clock() # For FPS and timers

        self.asset_loader = Asset_Loader(self) # For rendering assets


    def draw(self): # Drawing the items to the screen
        self.screen.fill(ROAD_COLOUR) # Temporary background which is a single colour

        self.all_sprites.draw(self.screen) # Drawing sprites to the screen (car, obstacles)

        self.clock.tick(FPS) # Setting the FPS
        pygame.display.update() # Refreshing the screen           

    def createTilemap(self): # Creating the tile map
        for i, row in enumerate(tilemap): 
            for j, column in enumerate(row):
                if column==1: # If "1" in tilemap
                    Block(self, j , i ) # Draw obstacle
                if column == 2: # If "2" in tilemap
                    Player(self, j , i ) # Draw player

    def main_menu(self): # For the menu
        pass

    def events(self): # For quitting
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: # If event = pressing the X button in top right
                self.running = False      # Quit game
            elif event.type == pygame.KEYDOWN:   # If key pressed
                if event.key == pygame.K_ESCAPE: # And that key is escape, then:
                    self.running = False         # Quit
                #testing sounds
                if event.key == pygame.K_z:
                    point()
                if event.key == pygame.K_x:
                    hit()
                if event.key == pygame.K_c:
                    loose()
                if event.key == pygame.K_v:
                    pause()
                if event.key == pygame.K_b:
                    unpause()
                    
                

    def update(self): # For refreshing the sprites
        self.all_sprites.update() # Update sprites (position, colour, anything in the function!)

    def main(self): # The main game
        while self.running: # While app running
            self.events()   # Call the functions
            self.draw()     # above in this order
            self.update()   # so the program works!
            
    def new(self): # For things you want from the start at the game: e.g. player
        self.all_sprites = pygame.sprite.LayeredUpdates() # Puts the sprites on screen

        self.createTilemap() # Creates a tilemap

if __name__ == "__main__": # If the name = the file you're running, will return True
    game = Game() # Calling the game class

    game.new()    # Calling the functions
    game.main()   # inside the class

    pygame.quit() # Quits out of pygame once main stops running
    sys.exit()    # Closes the window