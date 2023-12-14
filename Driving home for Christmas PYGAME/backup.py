#Making the window
import pygame #Importing the pygame module
import random #Importing random for random spawn times and random spawn positions
pygame.init() #Initialize the pygame module

win = pygame.display.set_mode((1000, 600)) #The windows geometry

pygame.display.set_caption("Driving home for Christmas") #The games window title

#Setting up movement variables
x = 50 #The players x position
y = 50 #The players y position
width = 50 #The players sprite width
height = 50 #The players sprite height
vel = 15 #The players speed


maxhealth = 10 #The players max health
current_health = 1 #THe players current health

#present variables
present_sprite_x = 0 #The x position of the present
present_sprite_y = 0 #The y position of the present

spawn_limit = 200 #How many presents can be on the screen at once
present_sprite_vel = 5 #The current sprite speed
max_present_vel = 100 #THe maximum speed of the presents
present_vel_increase = 1 #The increment of the presents speed

presents = [] #The presents on the screen
presents_destroyed = 0 #How many presents have been destroyed off screen
allow_increase = 0 #If the game can get harder or not
spawn_limit_increase = 2  # Initial increase value
presents_destroyed_previous = 0 
max_presents_destroyed = 500 #Maximum presents before the game stops getting harder
presents_to_remove = [] #Presents that need to be removed are appended here
present_spawn_timer = 0 
present_spawn_delay = random.randint(0, 1) #How long the interval is for the players spawning 20,100




road_line_x = 0 #The x value for the road lines
road_line_y = 0 #The y value for the road lines
lines = 5 #The amount of lines allowed to be drawn

road_lines = [] #Road lines will be appended here to later be deleted


#Function for checking for collision
def check_collision(present1, present2):
    distance = ((present1[0] - present2[0]) **2 + (present1[1] - present2[1])**2)**0.5 #Calculating distance relative to player
    return distance < 40



#Loading the sprites into the game

car_side_forward = pygame.image.load('Car-Right.png')
car_side_forward = pygame.transform.scale(car_side_forward, (98, 56))

car_side_backwards = pygame.image.load('Car-Left.png')
car_side_backwards = pygame.transform.scale(car_side_backwards, (98, 56))

#presents
presentsheight,presentswidth = 46.5,54

blue_present = pygame.image.load('blue-present.png')
blue_present = pygame.transform.scale(blue_present, (presentsheight, presentswidth))
green_present = pygame.image.load('green-present.png')
green_present = pygame.transform.scale(green_present, (presentsheight, presentswidth))
red_present = pygame.image.load('red-present.png')
red_present = pygame.transform.scale(red_present, (presentsheight, presentswidth))

# Rest of your code...

def get_primary_direction(keys):
    directions = {
        'up': keys[pygame.K_UP] or keys[pygame.K_w],
        'right': keys[pygame.K_RIGHT] or keys[pygame.K_d],
        'down': keys[pygame.K_DOWN] or keys[pygame.K_s],
        'left': keys[pygame.K_LEFT] or keys[pygame.K_a]
    }

    if directions['up']:
        return 'up'
    elif directions['right']:
        return 'right'
    elif directions['down']:
        return 'down'
    elif directions['left']:
        return 'left'
    else:
        return None


def sprite_change(direction):
    if direction == 'up':
        return car_side_forward
    elif direction == 'right':
        return car_side_forward
    elif direction == 'down':
        return car_side_forward
    elif direction == 'left':
        return car_side_backwards
    else:
        return car_side_forward

#Creating a main loop
run = True

while run:
    lines_vel = present_sprite_vel #The movement speed of the lines
    player_backforce = present_sprite_vel #The force against the player

    print(lines_vel, player_backforce, present_sprite_vel)
    pygame.time.delay(30)
    if x < 0:  # Left boundary
        x = 0
    elif x > 1000 - width:  # Right boundary
        x = 1000 - width
    if y < 0:  # Top boundary
        y = 0
    elif y > 600 - height:  # Bottom boundary
        y = 600 - height

    
    
    keys = pygame.key.get_pressed()
    primary_direction = get_primary_direction(keys)
    
    if not any((keys[pygame.K_UP], keys[pygame.K_DOWN], keys[pygame.K_LEFT], keys[pygame.K_RIGHT],
                keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_a], keys[pygame.K_d])):
        x -= lines_vel
        image_to_display = car_side_backwards  # Set the image for backward movement
    else:
        # Draw the appropriate image based on the primary direction
        image_to_display = sprite_change(primary_direction)

    present_spawn_timer += 3


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    
    

    win.fill((50,50,50))
    #All window changes must be changed under this point.

        
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= vel
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += vel
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= vel
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += vel

    # Draw the appropriate image based on the primary direction
    image_to_display = sprite_change(primary_direction)
    win.blit(image_to_display, (x, y))
        
    if presents_destroyed <= max_presents_destroyed:
        presents_destroyed_current = presents_destroyed // 10
        if presents_destroyed_current > presents_destroyed_previous:
            increase_amount = spawn_limit_increase * (presents_destroyed_current - presents_destroyed_previous)
            spawn_limit += increase_amount
            presents_destroyed_previous = presents_destroyed_current
            #print(f"Spawn limit increased by {increase_amount}")
            present_sprite_vel = present_vel_increase + present_sprite_vel
            #print(f"Speed increased to {present_sprite_vel}")
            
    if len(road_lines) < lines:
        if len(road_lines) == 0:
            road_line_x = 1200
        else:
            road_line_x = road_lines[-1][0] + 250
        road_lines.append([road_line_x,300])
    
    for road_line_for in road_lines[:]:
        road_line_sprite = pygame.Rect(road_line_for[0] - 20, road_line_for[1] - 20, 100, 20)
        pygame.draw.rect(win, (255,255,255), road_line_sprite)
        for road_line_for in road_lines:
            road_line_for[0] -= lines_vel
            if road_line_for[0] < -100:
                road_lines.remove(road_line_for)
    #drawing the character
    
    if present_spawn_timer >= present_spawn_delay and len(presents) < spawn_limit:
        # Reset timer and generate a new random delay for the next present spawn
        present_spawn_timer = 0
        present_spawn_delay = random.randint(5, 30)  # Set a new random delay
        spawn_side = random.randint(1, 5)  # Randomly choose a side: 1 for top, 2 for right, 3 for bottom, 4 for left
        present_color = random.randint(1, 3)  # Selects a number between 1 and 3

        if present_color == 1:
            present_image = blue_present
        elif present_color == 2:
            present_image = green_present
        else:
            present_image = red_present

        # Assign the present image based on the random number
        

        #print(f"spawn side:{spawn_side}")
        if spawn_side == 1:  # Top
            presents.append([1200, random.randint(10,100), present_image])  # Spawn on the right, top section
        elif spawn_side == 2:  # Middle
            presents.append([1200, random.randint(100,190), present_image])  # Spawn on the right, middle section
        elif spawn_side == 3:  # Bottom
            presents.append([1200, random.randint(280,370), present_image])  # Spawn on the right, bottom section
        elif spawn_side == 4:
            presents.append([1200, random.randint(370,450), present_image])
        else:  # Middle
            presents.append([1200, random.randint(450,540), present_image])  # Spawn on the right, middle section

        
    for present_sprite in presents[:]:
        #present_sprite_img = blue_present
        present_sprite_pos = present_sprite  # Replace this with the present_sprite position

        # Draw the present image
        #win.blit(present_sprite_img, (present_sprite_pos[0] - 20, present_sprite_pos[1] - 20))
        

        win.blit(present_sprite[2], (present_sprite_pos[0] - 20, present_sprite_pos[1] - 20))
        

        # Get the bounding rectangles of the player's character and the present image
        present_rect = pygame.Rect(present_sprite_pos[0] - 20, present_sprite_pos[1] - 20, 80, 80)
        player_rect = pygame.Rect(x, y, width, height)

        # Check for collision between the player and present rectangles
        present_sprite_pos[0] -= present_sprite_vel  # Move the present towards the left
        if present_sprite_pos[0] < -100:  # If the present goes off the left edge of the window
            presents.remove(present_sprite)

        if present_rect.colliderect(player_rect):
            current_health -= 1
            if current_health <= 0:
                run = False
        # Iterate through presents and update their movement
        # Iterate through presents and update their movement
        # Update presents' movement based on lines_vel
    for present_sprite in presents[:]:
        present_sprite[0] -= present_sprite_vel
        if present_sprite[0] < -100:
            presents.remove(present_sprite)
            presents_destroyed += 1
            #print(presents_destroyed)



        # Collision detection and handling presents to remove
        for present_sprite in presents[:]:
            for other_present in presents[:]:
                if present_sprite != other_present and check_collision(present_sprite, other_present):
                    if present_sprite not in presents_to_remove and other_present not in presents_to_remove:
                        presents_to_remove.extend([present_sprite, other_present])
                        
            
                        
        
        # Remove presents outside the iteration loop to avoid modifying the list during iteration
        for present in presents_to_remove:
            presents.remove(present)
        presents_to_remove.clear()
    
        
    #sprite = pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    

    
        
    print(lines_vel, player_backforce, present_sprite_vel)
    #Updating the window
    pygame.display.update()

pygame.quit()