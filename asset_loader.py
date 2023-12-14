import pygame
class Spritesheet:
    def __init__(self, file):  #Gets the file the user needs and allows them to save it as a variable
        self.sheet = pygame.image.load(file).convert()
    
    def get_sprite(self, x, y, width, height): # Then it will crop the sprite sheet by gettings the x axis, y axis the width of the image/sprite and height
        self.sheet = self.sheet
        sprite = pygame.Surface([width,height])
        sprite.blit(self.sheet, (0,0), (x,y,width,height))
        sprite.set_colorkey('black')
        return sprite

class Asset_Loader:
    def __init__(self, game):
        self.game = game
        self.width = 49 * 5   # Setting the width of the player
        self.height = 28 * 5  # Setting the height of the player
        
        # IMAGES
        self.player_image = pygame.image.load("Assets/Car/Car-Right.png").convert_alpha()
        self.player_image = pygame.transform.scale(self.player_image, (self.width, self.height))

        # CAR ANIMATIOn

        self.car_right_sheet = Spritesheet("Assets/Car/Car-spritesheet.png") # Gets the spritesheet

        # For every frame, make a variable.
        self.car_right_0 = Spritesheet.get_sprite(self.car_right_sheet, 0, 0, 49, 29)
        self.car_right_0 = pygame.transform.scale(self.car_right_0, (self.width, self.height)) # Setting the size of the image

        self.car_right_1 = Spritesheet.get_sprite(self.car_right_sheet, 50, 0, 49, 29)
        self.car_right_1 = pygame.transform.scale(self.car_right_1, (self.width, self.height))

        self.car_right_2 = Spritesheet.get_sprite(self.car_right_sheet, 0, 30, 49, 29)
        self.car_right_2 = pygame.transform.scale(self.car_right_2, (self.width, self.height))

        self.car_right_3 = Spritesheet.get_sprite(self.car_right_sheet, 50, 30, 49, 29)
        self.car_right_3 = pygame.transform.scale(self.car_right_3, (self.width, self.height))

        self.car_right_4 = Spritesheet.get_sprite(self.car_right_sheet, 0, 60, 49, 29)
        self.car_right_4 = pygame.transform.scale(self.car_right_4, (self.width, self.height))

        self.car_right_complete_list = [self.car_right_0, self.car_right_1, self.car_right_2, self.car_right_3, self.car_right_4]