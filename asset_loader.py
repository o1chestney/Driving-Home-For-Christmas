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

        # Car animation
        self.car_right_sheet = Spritesheet("Assets/Car/Car-spritesheet.png")       # Gets the spritesheet
        self.car_up_sheet = Spritesheet("Assets/Car/Car_back_spritesheet.png")   # Gets the spritesheet
        self.car_down_sheet = Spritesheet("Assets/Car/Car_front_spritesheet.png") # Gets the spritesheet

        # Add the frames to a variable
        self.right_animation = [Spritesheet.get_sprite(self.car_right_sheet, 0, 0, self.right_width, self.right_height),
                                Spritesheet.get_sprite(self.car_right_sheet, 49, 0, self.right_width, self.right_height),
                                Spritesheet.get_sprite(self.car_right_sheet, 0, 28, self.right_width, self.right_height),
                                Spritesheet.get_sprite(self.car_right_sheet, 49, 28, self.right_width, self.right_height),
                                Spritesheet.get_sprite(self.car_right_sheet, 0, 56, self.right_width, self.right_height)] 

        self.down_animation = [Spritesheet.get_sprite(self.car_down_sheet, 0, 0, self.width, self.height),
                                Spritesheet.get_sprite(self.car_down_sheet, 35, 0, self.width, self.height),
                                Spritesheet.get_sprite(self.car_down_sheet, 0, 30, self.width, self.height), 
                                Spritesheet.get_sprite(self.car_down_sheet, 35, 30, self.width, self.height), 
                                Spritesheet.get_sprite(self.car_down_sheet, 0, 60, self.width, self.height),   
                                Spritesheet.get_sprite(self.car_down_sheet, 35, 60, self.width, self.height)]  

        self.up_animation = [Spritesheet.get_sprite(self.car_up_sheet, 0, 0, self.width, self.height),
                                Spritesheet.get_sprite(self.car_up_sheet, 35, 0, self.width, self.height),
                                Spritesheet.get_sprite(self.car_up_sheet, 0, 30, self.width, self.height), 
                                Spritesheet.get_sprite(self.car_up_sheet, 35, 30, self.width, self.height), 
                                Spritesheet.get_sprite(self.car_up_sheet, 0, 60, self.width, self.height),   
                                Spritesheet.get_sprite(self.car_up_sheet, 35, 60, self.width, self.height)]           
        
        # Map
        self.tilemap = Spritesheet("Assets/Map/Tilemap.png") # Gets the spritesheet

        self.barrier_top = pygame.image.load("Assets/Car/Car-Right.png").convert_alpha()