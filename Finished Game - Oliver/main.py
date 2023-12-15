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
        self.health = 30
        self.image_forward = pygame.transform.scale(pygame.image.load('Car-Right.png'), (98, 56))
        self.image_backward = pygame.transform.scale(pygame.image.load('Car-Left.png'), (98, 56))
        self.direction = 'right'
        self.backforce = 5

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
                self.x -= self.backforce
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
        self.presents_destroyed = 0
        self.max_presents_destroyed = 50
        self.present_vel = 5
        self.spawn_timer_increase = 1
        self.speed_increased = False

    def update(self):
        self.spawn_timer += self.spawn_timer_increase
        if self.spawn_timer >= self.spawn_delay and len(self.presents) < 200:
            self.spawn_timer = 0
            self.spawn_delay = random.randint(5, 30)
            spawn_side = random.randint(1, 5)
            present_color = random.randint(1, 3)
            present_image = self.get_present_image(present_color)
            self.spawn_present(spawn_side, present_image)

        for present in self.presents[:]:
            present[0] -= self.present_vel
            if present[0] < -80:
                self.presents.remove(present)
                self.presents_destroyed += 1

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
        self.lines_vel = 5
    def update(self):
        if len(self.lines) < 5:
            if len(self.lines) == 0:
                x = 1200
            else:
                x = self.lines[-1][0] + 250
            self.lines.append([x, 300])

        for road_line in self.lines[:]:
            road_line[0] -= self.lines_vel
            if road_line[0] < -100:
                self.lines.remove(road_line)


class Menu:
    def __init__(self, options):
        self.options = options
        self.font = pygame.font.Font(None, 50)
        self.selected = 0
        self.is_active = True

    def draw(self,win):
        
        if self.is_active:
            win.blit(gif_image, gif_rect)
            for i, option in enumerate(self.options):
                
                color = (0, 255, 0) if i == self.selected else (0, 0, 0)
                text = self.font.render(option, True, color)
                text_rect = text.get_rect(center=(500, 200 + i * 40))
                win.blit(text, text_rect)
                
            title = self.font.render("Driving Home For Christmas", True, (0,255,0))
            title_rect = text.get_rect(center=(325, 100))
            win.blit(title, title_rect)
            control = self.font.render("Use arrow keys to select then press enter", True, (0,255,0))
            control_rect = text.get_rect(center=(250, 500))
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

menu = Menu(["Play", "Instructions", "Quit"])

run = True
clock = pygame.time.Clock()

current_state = "menu"

gif_image = pygame.image.load('menu.gif')  # Replace 'example.gif' with your GIF file path
gif_image = pygame.transform.scale(gif_image, (1000, 600))
# Get the rect of the loaded GIF to position it on the screen
gif_rect = gif_image.get_rect(center=(1000 // 2, 600 // 2))

while run:
    fps = clock.get_fps()
    rounded = round(fps)
    clock.tick(45)
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
                    current_state = "instructions"
                    print("Instructions selected!")
                elif selected_option == 2:  # If "Quit" is selected
                    current_state = "quitw"
                    print("Quit selected!")

    if current_state == "game":
        car.update(keys)
        present_manager.update()
        road_lines.update()

        win.fill((50, 50, 50))  # Fill the window with a background color

        if present_manager.presents_destroyed % 10 == 0 and present_manager.presents_destroyed > 0:
            if not present_manager.speed_increased:
                present_manager.present_vel += 1  # Increase present velocity
                road_lines.lines_vel += 1  # Increase road lines velocity
                car.backforce += 1  # Increase player's backforce
                present_manager.spawn_timer_increase += 0.05
                print(f"Difficulty increase, {present_manager.present_vel},{road_lines.lines_vel},{car.backforce}, {present_manager.spawn_timer_increase}")
                present_manager.speed_increased = True
        if present_manager.presents_destroyed % 10 != 0:
            present_manager.speed_increased = False
        
        background_image = pygame.image.load('bg.png')
        background_rect = background_image.get_rect()

        start_x = (road_lines.lines[0][0] % background_rect.width) - background_rect.width

        for x in range(start_x, win.get_width(), background_rect.width):
            for y in range(0, win.get_height(), background_rect.height):
                win.blit(background_image, (x, y))

        for road_line in road_lines.lines:
            pygame.draw.rect(win, (255, 255, 255), pygame.Rect(road_line[0], road_line[1], 100, 20))

        for present in present_manager.presents:
            win.blit(present[2], (present[0], present[1]))

        display_lives = menu.font.render(f"Lives: {car.health}", True, (0,255,0))
        display_lives_rect = display_lives.get_rect(center=(700, 550))
        win.blit(display_lives, display_lives_rect)

        display_presents = menu.font.render(f"Missed Presents: {present_manager.presents_destroyed}", True, (0,255,0))
        display_presents_rect = display_presents.get_rect(center=(700, 500))
        win.blit(display_presents, display_presents_rect)

        fps_font = pygame.font.Font(None, 36)
        display_fps = fps_font.render(f"FPS: {rounded}", True, (0,255,0))
        display_fps_rect = display_fps.get_rect(center=(800, 50))
        win.blit(display_fps, display_fps_rect)

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
    
    if current_state == "instructions":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        

        win.fill((0,0,0))
        text = "This is an endless scroller game, the aim is to avoid as many presents as you can.\nYou have a certain amount of lives which decrease when you hit into a present\nMove by using the arrow keys or w,a,s,d.\nHave Fun!\n(Close and reopen the game and click play)"
        font = pygame.font.Font(None, 36)
        text_lines = text.split("\n")
        text_surfaces = [font.render(line, True, (255, 255, 255)) for line in text_lines]

        text_height = sum(surface.get_height() for surface in text_surfaces)
        y_pos = (1000 - 600) // 2
        for surface in text_surfaces:
            text_width = surface.get_width()
            x_pos = (1000 - text_width) // 2  # Center horizontally
            win.blit(surface, (x_pos, y_pos))
            y_pos += surface.get_height()
    
    if current_state == "quit":
        run = False

    menu.draw(win)
    

    
    pygame.display.update()

pygame.quit()