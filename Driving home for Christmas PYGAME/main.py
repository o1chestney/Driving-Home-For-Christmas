import pygame
import random


#I hadn't realised that the game model had changed but this is what i have made so far, there just needs to be a few more things added.


class Car:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.width = 50
        self.height = 50
        self.vel = 15
        self.health = 3
        self.image_forward = pygame.transform.scale(pygame.image.load('Car-Right.png'), (98, 56))
        self.image_backward = pygame.transform.scale(pygame.image.load('Car-Left.png'), (98, 56))
        self.direction = 'right'

    def update(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.y - self.vel > 0:
                self.y -= self.vel
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.y + self.height + self.vel < 600:
                self.y += self.vel
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.x - self.vel > 0:
                self.x -= self.vel
                self.direction = 'left'
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.x + self.width + self.vel < 1000:
                self.x += self.vel
                self.direction = 'right'
        if not any((keys[pygame.K_UP], keys[pygame.K_DOWN], keys[pygame.K_LEFT], keys[pygame.K_RIGHT],
            keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_a], keys[pygame.K_d])):
            if self.x - self.vel > 0:
                self.x -= 5
                self.direction = "right"



    def get_image(self):
        if self.direction == 'left':
            return self.image_backward
        return self.image_forward

class PresentManager:
    def __init__(self):
        self.presents = []
        self.spawn_timer = 0
        self.spawn_delay = random.randint(5, 30)
        self.blue_present = pygame.transform.scale(pygame.image.load('blue-present.png'), (80, 80))
        self.green_present = pygame.transform.scale(pygame.image.load('green-present.png'), (80, 80))
        self.red_present = pygame.transform.scale(pygame.image.load('red-present.png'), (80, 80))

    def update(self):
        self.spawn_timer += 1.5
        if self.spawn_timer >= self.spawn_delay and len(self.presents) < 200:
            self.spawn_timer = 0
            self.spawn_delay = random.randint(5, 30)
            spawn_side = random.randint(1, 5)
            present_color = random.randint(1, 3)
            present_image = self.get_present_image(present_color)
            self.spawn_present(spawn_side, present_image)

        for present in self.presents[:]:
            present[0] -= 5
            if present[0] < -80:
                self.presents.remove(present)

    def get_present_image(self, color):
        if color == 1:
            return self.blue_present
        elif color == 2:
            return self.green_present
        else:
            return self.red_present

    def spawn_present(self, side, image):
        if side == 1:  # Top
            self.presents.append([1200, random.randint(10,100), image])  # Spawn on the right, top section
        elif side == 2:  # Middle
            self.presents.append([1200, random.randint(100,190), image])  # Spawn on the right, middle section
        elif side == 3:  # Bottom
            self.presents.append([1200, random.randint(280,370), image])  # Spawn on the right, bottom section
        elif side == 4:
            self.presents.append([1200, random.randint(370,450), image])
        else:  # Middle
            self.presents.append([1200, random.randint(450,540), image])  # Spawn on the right, middle section

class RoadLines:
    def __init__(self):
        self.lines = []

    def update(self):
        if len(self.lines) < 5:
            if len(self.lines) == 0:
                x = 1200
            else:
                x = self.lines[-1][0] + 250
            self.lines.append([x, 300])

        for road_line in self.lines[:]:
            road_line[0] -= 5
            if road_line[0] < -100:
                self.lines.remove(road_line)


class Menu:
    def __init__(self, options):
        self.options = options
        self.font = pygame.font.Font(None, 36)
        self.selected = 0
        self.is_active = True

    def draw(self,win):
        if self.is_active:
            for i, option in enumerate(self.options):
                color = (255, 255, 255) if i == self.selected else (128, 128, 128)
                text = self.font.render(option, True, color)
                text_rect = text.get_rect(center=(500, 200 + i * 40))
                win.blit(text, text_rect)
            title = self.font.render("Driving Home For Christmas", True, (0,255,0))
            title_rect = text.get_rect(center=(375, 100))
            win.blit(title, title_rect)
            control = self.font.render("Use arrow keys to select then press enter", True, (0,255,0))
            control_rect = text.get_rect(center=(375, 500))
            win.blit(control, control_rect)

    def handle_input(self, event):
        if self.is_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected = (self.selected - 1) % len(self.options) 
                elif event.key == pygame.K_DOWN:
                    self.selected = (self.selected + 1) % len(self.options)  # Move selection down
                elif event.key == pygame.K_RETURN:  # Enter key to confirm selection
                    self.is_active = False
                    return self.selected
                
        return None





pygame.init()
win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Driving home for Christmas")

car = Car()
present_manager = PresentManager()
road_lines = RoadLines()

menu = Menu(["Play", "Options", "Quit"])

run = True
clock = pygame.time.Clock()

current_state = "menu"

while run:
    clock.tick(30)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if current_state == "menu":  # Game state is menu
            selected_option = menu.handle_input(event)
            if selected_option is not None:
                if selected_option == 0:  # If "Play" is selected
                    current_state = "game"  # Change game state to the main game
                    print("Play selected!")
                elif selected_option == 1:  # If "Options" is selected
                    current_state = "options"
                    print("Options selected!")
                elif selected_option == 2:  # If "Quit" is selected
                    current_state = "quit"
                    print("Quit selected!")

    if current_state == "game":
        car.update(keys)
        present_manager.update()
        road_lines.update()

        win.fill((50, 50, 50))  # Fill the window with a background color

        background_image = pygame.image.load('bg.png')
        background_rect = background_image.get_rect()
        for x in range(0, win.get_width(), background_rect.width):
            for y in range(0, win.get_height(), background_rect.height):
                win.blit(background_image, (x, y))

        for road_line in road_lines.lines:
            pygame.draw.rect(win, (255, 255, 255), pygame.Rect(road_line[0], road_line[1], 100, 20))

        for present in present_manager.presents:
            win.blit(present[2], (present[0], present[1]))

        # Check for collision between car and presents
        car_rect = pygame.Rect(car.x, car.y, car.width, car.height)
        for present in present_manager.presents[:]:
            present_rect = pygame.Rect(present[0], present[1], 80, 80)
            if car_rect.colliderect(present_rect):
                print("HIT")
                present_manager.presents.remove(present)
                # Perform actions for collision 
                car.health -= 1
                if car.health <= 0:
                    run = False
        

        win.blit(car.get_image(), (car.x, car.y))
    
    if current_state == "options":
        pass
    
    if current_state == "quit":
        run = False

    menu.draw(win)
    

    
    pygame.display.update()

pygame.quit()