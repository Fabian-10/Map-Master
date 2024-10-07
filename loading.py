import pygame
import sys
import math
import time

# Function to run the rotating Earth animation
def rotating_earth_animation(screen, duration=2):  # Duration in seconds
    # Set up the screen
    screen_width = 1100
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Rotating Earth Animation")

    # Load the Earth image and scale it down
    earth_image = pygame.image.load('earth.png')  # Replace with the path to your Earth image
    earth_image = pygame.transform.scale(earth_image, (300, 160))

    # Center coordinates for the Earth image
    center_x = screen_width // 2
    center_y = screen_height // 2

    # Define colors
    bg_color = (0, 0, 0)  # Black background

    # Rotation speed
    rotation_speed = 1  # Controls how fast the Earth rotates

    # Main loop for the animation
    loading = True
    angle = 0

    # Start time to track the duration
    start_time = time.time()

    while loading:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loading = False
                pygame.quit()
                sys.exit()

        # Automatically stop after 'duration' seconds
        if time.time() - start_time > duration:
            loading = False
            pygame.quit()
            return  # You can return control to the calling function

        # Clear the screen with the background color
        screen.fill(bg_color)

        # Rotate the Earth image
        rotated_earth = pygame.transform.rotate(earth_image, angle)
        rotated_rect = rotated_earth.get_rect(center=(center_x, center_y))

        # Draw the rotated Earth image on the screen
        screen.blit(rotated_earth, rotated_rect)

        # Update the angle for the rotation
        angle -= rotation_speed  # Negative to rotate counter-clockwise

        # Update the display
        pygame.display.flip()

        # Control the speed of the animation
        time.sleep(0.01)

# Example of calling the function
# screen is passed when this function is called, or you can leave it as None
# rotating_earth_animation(screen, duration=10)

# Call the game function to run
if __name__ == "__main__":
    rotating_earth_animation(None)