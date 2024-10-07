import pygame
import sys

# importing option_screen from other file to be able to select region
from Team3 import option_screen

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1100
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Project Fourier: Map Master")

# Load the background image
bg_image = pygame.image.load('Notepgwallpaper.jpeg')  # Replace with your image path
bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height))  # Scale to fit the screen
#fun_image = pygame.image.load("image.file")
#fun_image = pygame.transform

# Define colors
button_color = (176,196,222)  # Color for buttons
border_color = (100,149,237)
hover_color = (85, 107, 47)    # Hover color for buttons
text_color = (100,149,237)  # Color for text
title_color = (0, 0, 0)  # Color for the border title
titlemap_color = (85, 107, 47) # Color for the Geo of GeoMatch
titlemaster_color = (100, 149, 237) # Color for the Match of GeoMatch
titleborder_color = (0, 0, 0)

# Set up fonts
font = pygame.font.SysFont("Bradley Hand ITC", 40, bold = True)
title_font = pygame.font.SysFont("Lucida Handwriting", 110, bold = True)  # Larger font for title

# Button dimensions
button_width = 400
button_height = 60

# Create button rectangles centered on the screen
button1 = pygame.Rect((screen_width - button_width) // 2, 400, button_width, button_height)
button2 = pygame.Rect((screen_width - button_width) // 2, 525, button_width, button_height)
button3 = pygame.Rect((screen_width - button_width) // 2, 525, button_width, button_height)
button4 = pygame.Rect((screen_width - button_width) // 2, 400, button_width, button_height)

def draw_rounded_rect(surface, color, rect, border_radius):
    pygame.draw.rect(surface, color, rect, border_radius=border_radius)

def draw_button(rect, text, is_hovering):
    # set the color of the button based on whether the user is hovering the mouse or not
    color = hover_color if is_hovering else button_color

    #draw rounded corner button
    draw_rounded_rect(screen, color, rect, border_radius=30)
    border_rect = rect.inflate(10, 10) # this increases the size by 10 pixles 
    # draw the border of the buttons to be slightly larger 
    draw_rounded_rect(screen, border_color, border_rect, border_radius=35)
    draw_rounded_rect(screen, color, rect, border_radius=30)  # Draw button

    # Center the text within the button
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)  # Center the text
    screen.blit(text_surface, text_rect)

def draw_title(part1, part2):

     # Render the first part of the title
    map_surface = title_font.render(part1, True, titlemap_color)
    map_rect = map_surface.get_rect(center=(screen_width // 2 - 210, 200))  # Adjust position for "Map"
    map_border_surface = title_font.render(part1, True, titleborder_color)
    map_border_rect = map_border_surface.get_rect(center=(screen_width // 2 - 210, 212))
    map_border_rect = map_border_rect.inflate(10, 10) 

    # Render the second part of the title
    master_surface = title_font.render(part2, True, titlemaster_color)
    master_rect = master_surface.get_rect(center=(screen_width // 2 + 165, 200))  # Adjust position for "Master"
    master_border_surface = title_font.render(part2, True, titleborder_color)
    master_border_rect = master_border_surface.get_rect(center=(screen_width // 2 + 165, 212))
    master_border_rect = master_border_rect.inflate(10, 10) 
    # Draw the title parts on the screen
    screen.blit(map_border_surface, map_border_rect)
    screen.blit(map_surface, map_rect) 
    screen.blit(master_border_surface, master_border_rect)
    screen.blit(master_surface, master_rect) 
   

# Main loop
run = True
while run:
    GameMode = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                print("Capitol Game")
                option_screen(screen) # calling option_screen from other file to choose region
            elif button2.collidepoint(event.pos):
                GameMode = True
                print("Flag Game")
                option_screen(screen) # calling option_screen from other file to choose region
                
    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()
    
    # Check if mouse is hovering over buttons
    button1_hover = button1.collidepoint(mouse_pos)
    button2_hover = button2.collidepoint(mouse_pos)

    # Drawing
    screen.blit(bg_image, (0, 0))  # Draw the background image
    draw_title("Map", "Master")  # Draw the title
    draw_button(button3, "Flag Frenzy", button2_hover) #creating a border for the button
    draw_button(button4, "Flag Frenzy", button1_hover) #creating a border for the button
    draw_button(button1, "Capitol Craze", button1_hover)
    draw_button(button2, "Flag Frenzy", button2_hover)
    
    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()
