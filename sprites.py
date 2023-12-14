import pygame
import math

from config import *

class Player(pygame.sprite.Sprite):# Creating the player class
    def __init__(self, game, x, y):# And initialising it 
        self.game=game                                  # Allows you to use variables from the game class
        self._layer=PLAYER_LAYER                        # Setting the layer of the player
        self.groups=self.game.all_sprites               # Adding the player to the "all_sprites" group
        pygame.sprite.Sprite.__init__(self, self.groups)# Initialises the sprite 

        self.x = x * TILESIZE # Setting the x coordinate of the player
        self.y = y * TILESIZE # Setting the y coordinate of the player
        self.width = 49 * 5   # Setting the width of the player facing right
        self.height = 29 * 5  # Setting the height of the player facing right

        self.image = self.game.asset_loader.player_image # Loading the player's image
        self.image = pygame.transform.scale(self.image, (self.width, self.height)) # Setting the size of the image

        self.anim_state = 'idle' # Car is unmoving to begin
        self.animation_loop = 1
        self.facing = 'right'

        self.x_change = 0     # Setting the value for movement to 0 as default
        self.y_change = 0     # Setting the value for movement to 0 as default

        self.rect=self.image.get_rect() # Getting the rect for the player - for collision (basically an invisible box)
        self.rect.x=self.x                  # Getting the x coordinate for the rect
        self.rect.y=self.y                  # Getting the y coordinate for the rect

    def update(self): # Updating the player
        self.movement() # Calling the movement function
        self.animate()

        self.rect.x += self.x_change # Moving the player's x coordinate
        self.collision("x") # When player moved, checks if there's collision on x
        self.rect.y += self.y_change # Moving the player's y coordinate
        self.collision("y") # When player moved, checks if there's collision on y
       
        self.x_change = 0 # Resetting the movement value to 0 
        self.y_change = 0 

    def animate(self):
        if self.facing == "right":
            self.width = 49 * 5   # Setting the width of the player facing right
            self.height = 29 * 5  # Setting the height of the player facing right

            if self.animation_loop >= 5:
                    self.animation_loop = 0

            if self.x_change == 0:
                self.image = self.game.asset_loader.right_animation[math.floor(self.animation_loop)] # Loading the player's image
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
            else:
                self.image = self.game.asset_loader.right_animation[math.floor(self.animation_loop)]
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.animation_loop += 0.1
                if self.animation_loop >= 5:
                    self.animation_loop = 0
            
        if self.facing == "up":
            self.width = 35 * 5
            self.height = 30 * 5
            if self.y_change == 0:
                self.image = self.game.asset_loader.up_animation[math.floor(self.animation_loop)]
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
            else:
                self.image = self.game.asset_loader.up_animation[math.floor(self.animation_loop)]
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.animation_loop += 0.1
                if self.animation_loop >= 6:
                    self.animation_loop = 0
        
        if self.facing == "down":
            self.width = 35 * 5
            self.height = 30 * 5
            if self.y_change == 0:
                self.image = self.game.asset_loader.down_animation[math.floor(self.animation_loop)]
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
            else:
                self.image = self.game.asset_loader.down_animation[math.floor(self.animation_loop)]
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.animation_loop += 0.1
                if self.animation_loop >= 6:
                    self.animation_loop = 0

    def movement(self): # Moving the player
        keys=pygame.key.get_pressed() 

        if keys[pygame.K_LEFT] or keys[pygame.K_a]: # If the left arrow key or the A key is pressed
            self.facing = "left"                      # set the direction of the player
            for sprite in self.game.all_sprites:    # move all the sprites
                sprite.rect.x += PLAYER_SPEED       # to the right, to give the illusion of moving
            self.x_change-= PLAYER_SPEED

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: # If the right arrow key or the D key is pressed
            self.facing = "right"                     # set the direction of the player
            for sprite in self.game.all_sprites:     # move all the sprites
                sprite.rect.x -= PLAYER_SPEED        # to the left to give the illusion of moving
            self.x_change += PLAYER_SPEED 

        if keys[pygame.K_UP] or keys[pygame.K_w]: # If the up arrow key or the W key is pressed
            for sprite in self.game.all_sprites:  # move all the sprites
                self.facing = "up"                  # set the direction of the player
                sprite.rect.y += PLAYER_SPEED     # down to give the illusion of moving
            self.y_change-=PLAYER_SPEED

        if keys[pygame.K_DOWN] or keys[pygame.K_s]: # If the up arrow key or the W key is pressed
            self.facing = "down"                      # set the direction of the player
            for sprite in self.game.all_sprites:    # move all the sprites
                sprite.rect.y -= PLAYER_SPEED       # up to give the illusion of moving
            self.y_change += PLAYER_SPEED
    
    def collision(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    for sprite in self.game.all_sprites: # This keeps the camera on the player
                        sprite.rect.x += PLAYER_SPEED
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    for sprite in self.game.all_sprites: # This keeps the camera on the player
                        sprite.rect.x -= PLAYER_SPEED
                    self.rect.x = hits[0].rect.right 

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    for sprite in self.game.all_sprites: # This keeps the camera on the player
                        sprite.rect.y += PLAYER_SPEED
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    for sprite in self.game.all_sprites: # This keeps the camera on the player
                        sprite.rect.y -= PLAYER_SPEED
                    self.rect.y = hits[0].rect.bottom

class Block(pygame.sprite.Sprite): # Creating the block class
    def __init__(self, game, x, y): # Initialising it
        self.game = game # Calling
        self._layer = BLOCK_LAYER # Setting the layer for the block objects
        self.groups = self.game.all_sprites, self.game.blocks # Adding all groups to a big group
        pygame.sprite.Sprite.__init__(self, self.groups) # Initialises the sprite 

        self.x=x*TILESIZE    # Setting the x coordinate of the block
        self.y=y*TILESIZE    # Setting the y coordinate of the block
        self.width=TILESIZE  # Setting the width of the block
        self.height=TILESIZE # Setting the height of the block

        self.image = pygame.Surface([self.width, self.height]) # Creating a temporary square
        self.image.fill("red")  # Filling it with red

        self.rect=self.image.get_rect() # Creating a rect for collision
        self.rect.x=self.x # Setting the rect x coordinate
        self.rect.y=self.y # Setting the rect y coordinate

class Random_block(pygame.sprite.Sprite): # Creating the block class
    def __init__(self, game, x, y): # Initialising it
        self.game = game # Calling
        self._layer = BLOCK_LAYER # Setting the layer for the block objects
        self.groups = self.game.all_sprites # Adding all groups to a big group
        pygame.sprite.Sprite.__init__(self, self.groups) # Initialises the sprite 

        self.x=x*TILESIZE    # Setting the x coordinate of the block
        self.y=y*TILESIZE    # Setting the y coordinate of the block
        self.width=TILESIZE  # Setting the width of the block
        self.height=TILESIZE # Setting the height of the block

        self.image = pygame.Surface([self.width, self.height]) # Creating a temporary square
        self.image.fill("blue")  # Filling it with red

        self.rect=self.image.get_rect() # Creating a rect for collision

# class CameraGroup(pygame.sprite.Group):
#     def __init__(self):
#         super().__init__()
#         self.display_surface = pygame.display.get_surface()