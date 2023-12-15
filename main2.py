# Importing ---------------
import pygame, sys, random

from config import *
from sprites import *
from asset_loader import *

# NOTE TO FIRST YEARS:
# I'm sorry I've not been the best with communication! It's not been a great week for me,
# but Oliver your code looks great! 
# It's very impressive you were able to make the menu and everything, I'm sorry I kind of went off on my own
# I think it would benefit from some commenting though, and Layla the code for the music is great! You've
# both done very well despite the lack of communication on my end. Idk if you'll even see this, but if you do, 
# have a great half term & happy holidays! 

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
                if column == 0:
                    if random.randint(1,2) == 1:
                        Road_Block(self, j, i, "road_2")
                    else:
                        Road_Block(self, j, i, "road_1")
                if column==1: # If "1" in tilemap
                    Block(self, j , i, "barrier_top") # Draw top barrier
                if column==2: # #barrier_left
                    Block(self, j , i, "barrier_left") # Draw leftbarrier
                if column == 3: 
                    Block(self, j, i, "finish") # Finish line
                if column == 4: # barrier_bottom
                    Block(self, j , i, "barrier_bottom") # Draw bottom barrier
                if column == "P": # If "P" in tilemap
                    Road_Block(self, j, i, "road_1")
                    Player(self, j , i ) # Draw player
                if column == 5:
                    Road_Block(self, j, i, "top_road_barrier")
                if column == 6:
                    Road_Block(self, j, i, "bottom_road")
                if column == 7:
                    Road_Block(self, j, i, "middle_road")
                if column == 8:
                    Block(self, j, i, "path")

    
    def main_menu(self): # For the menu
        pass

    def events(self): # For quitting
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: # If event = pressing the X button in top right
                self.running = False      # Quit game
            elif event.type == pygame.KEYDOWN:   # If key pressed
                if event.key == pygame.K_ESCAPE: # And that key is escape, then:
                    self.running = False         # Quit

    def update(self): # For refreshing the sprites
        self.all_sprites.update() # Update sprites (position, colour, anything in the function!)

    def main(self): # The main game
        while self.running: # While app running
            self.events()   # Call the functions
            self.draw()     # above in this order
            self.update()   # so the program works!
            
    def new(self): # For things you want from the start at the game: e.g. player
        self.all_sprites = pygame.sprite.LayeredUpdates() # Adds the sprites to a group
        self.blocks = pygame.sprite.LayeredUpdates() # Adds the blocks to a group
        self.road_blocks = pygame.sprite.LayeredUpdates()

        self.createTilemap() # Creates a tilemap

if __name__ == "__main__": # If the name = the file you're running, will return True
    game = Game() # Calling the game class

    game.new()    # Calling the functions
    game.main()   # inside the class

    pygame.quit() # Quits out of pygame once main stops running
    sys.exit()    # Closes the window