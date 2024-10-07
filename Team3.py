""" 
https://www.geeksforgeeks.org/introduction-to-pygame/ - intro to pygame
https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/ - using a button
"""

import pygame
import sys
from mygame_euro import start_capital_game_euro  # Import the game function
from mygame_asia import start_capital_game_asia  # Import the game function
from mygame_africa import start_capital_game_africa  # Import the game function
from loading import rotating_earth_animation  # Import the game function
from europeF import start_flag_game_euro
from mygame_africa_flag import start_flag_game_africa


# defining as function to link with other files
def option_screen(screen):
    # Initialize Pygame
    pygame.init()

    # Set up the screen
    screen_width = 1100
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Interactive Buttons with Movable Text")
    bg_image = pygame.image.load('Notepgwallpaper.jpeg')  # Replace with your image path
    bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height))  # Scale to fit the screen
    fun_image = pygame.image.load("WorldMap.png")
    fun_image = pygame.transform.scale(fun_image, (screen_width*.75, screen_height*.75))


    # Define colors
    button1_color = (255, 0, 0, 0)  # Color for Button 1 (continent 1)
    button2_color = (0, 255, 0, 0)   # Color for Button 2 (continent 2)
    button3_color = (0, 0, 255, 0)  # Color for Button 2 (continent 3)
    button4_color = (0, 0, 0, 0)   # Color for Button 2 (continent 4)
    button1_x = 200
    button1_y = 250
    button2_x = 500
    button2_y = 200
    button3_x = 200
    button3_y = 475
    button4_x = 500
    button4_y = 645
    title_color = (0, 0, 0)  # Color for the border title
    titlemap_color = (85, 107, 47) # Color for the Geo of GeoMatch
    titlemaster_color = (100, 149, 237) # Color for the Match of GeoMatch
    titleborder_color = (0, 0, 0)


    # Set up fonts
    #font = pygame.font.SysFont("Goudy Stout", 30)
    title_font = pygame.font.SysFont("Lucida Handwriting", 80, bold=True)   # Larger font for title

    # Create button rectangles with unique positions
    button1 = pygame.Surface((300, 225), pygame.SRCALPHA)   # Europe
    button2 = pygame.Surface((450, 445), pygame.SRCALPHA)    # Asia
    button3 = pygame.Surface((300, 250), pygame.SRCALPHA)  # Africa
    button4 = pygame.Surface((450, 150), pygame.SRCALPHA)    # Australia

    button_rect1 = button1.get_rect(topleft=(button1_x, button1_y))
    button_rect2 = button2.get_rect(topleft=(button2_x, button2_y))
    button_rect3 = button3.get_rect(topleft=(button3_x, button3_y))
    button_rect4 = button4.get_rect(topleft=(button4_x, button4_y))

    # Initialize text positions
    #text1_pos = [button1.x + 20, button1.y + 5]   # Initial position for Text 1 (Europe)
    #text2_pos = [button2.x + 20, button2.y + 5]   # Initial position for Text 2 (Asia)
    #text3_pos = [button3.x + 20, button3.y + 5]   # Initial position for Text 3 (Africa)
    #text4_pos = [button4.x + 20, button4.y + 5]   # Initial position for Text 4 (Aulstralia)

    def draw_button(Surface, button_color, x, y):
        Surface.fill(button_color)
        screen.blit(Surface, (x, y))
        #text_surface = font.render(text, True, text_color)
        #screen.blit(text_surface, text_pos)

    def draw_title(part1, part2):

     # Render the first part of the title
        map_surface = title_font.render(part1, True, titlemap_color)
        map_rect = map_surface.get_rect(center=(screen_width // 2 - 210, 100))  # Adjust position for "Map"
        map_border_surface = title_font.render(part1, True, titleborder_color)
        map_border_rect = map_border_surface.get_rect(center=(screen_width // 2 - 210, 112))
        map_border_rect = map_border_rect.inflate(10, 10) 

        # Render the second part of the title
        master_surface = title_font.render(part2, True, titlemaster_color)
        master_rect = master_surface.get_rect(center=(screen_width // 2 + 165, 100))  # Adjust position for "Master"
        master_border_surface = title_font.render(part2, True, titleborder_color)
        master_border_rect = master_border_surface.get_rect(center=(screen_width // 2 + 165, 112))
        master_border_rect = master_border_rect.inflate(10, 10) 
    # Draw the title parts on the screen
        screen.blit(map_border_surface, map_border_rect)
        screen.blit(map_surface, map_rect) 
        screen.blit(master_border_surface, master_border_rect)
        screen.blit(master_surface, master_rect) 
    # Main loop
    run = True
    from Team2 import GameMode # importing bools indicating which game mode to play
    while run:
        for event in pygame.event.get():
            Europe = False
            Asia = False
            Africa = False
            Aulstralia = False
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect1.collidepoint(event.pos):
                    print("Europe!")
                    Europe = True
                    rotating_earth_animation(screen) # Call loading screen
                    if GameMode == False:
                        start_capital_game_euro(screen)  # Call the game function when button is clicked
                    else:
                        start_flag_game_euro(screen)
                elif button_rect2.collidepoint(event.pos):
                    print("Asia!")
                    aisa = True
                    rotating_earth_animation(screen) # Call loading screen
                    start_capital_game_asia(screen) # Call the game function when button is clicked
                elif button_rect3.collidepoint(event.pos):
                    print("Africa!")
                    Africa = True
                    rotating_earth_animation(screen) # Call loading screen
                    if GameMode == False:
                        start_capital_game_africa(screen) # Call the game function when button is clicked
                    else:
                        start_flag_game_africa(screen)
                elif button_rect4.collidepoint(event.pos):
                    print("Australia!")
                    Autralia = True

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()
        
        # Check if mouse is hovering over buttons
        #button1_hover = button1.collidepoint(mouse_pos)
        #button2_hover = button2.collidepoint(mouse_pos)
        #button3_hover = button3.collidepoint(mouse_pos)
        #button4_hover = button4.collidepoint(mouse_pos)

        # Drawing
        screen.blit(bg_image, (0, 0))
        screen.blit(fun_image, (200, screen_height*.25))
        draw_title("Pick", "Continent")  # Draw the title
        draw_button(button1, button1_color, button1_x, button1_y)
        draw_button(button2, button2_color, button2_x, button2_y)
        draw_button(button3, button3_color, button3_x, button3_y)
        draw_button(button4, button4_color, button4_x, button4_y)

        pygame.display.flip()  # Update the display