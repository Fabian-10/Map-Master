# import the pygame module
import pygame
import random
# import pygame.locals for easier 
# access to key coordinates
from pygame.locals import *

# initializing dictionary for european countries and capitals
mydiceuro = {
	"Turkey" : "Ankara",
	"United Kingdom" : "London",
	"Ireland" : "Dublin",
	"Spain" : "Madrid",
	"Russia" : "Moscow",
	"France" : "Paris",
	"Sweden" : "Stockholm",
	"Netherlands" : "Amsterdam"
}

def start_capital_game_euro(screen):
	# The next 10 variables are global
	# if you move them from here, the game will not run
	inc = 85 # determine the spaces between the square in the vertical position

	# how far are the going to be from the right side of the screen
	# horizontalStartL and horizontalStartR are variables used later for checking mouse position in game
	horizontalCount = 40
	horizontalCap = 400
	horizontalStartL = horizontalCount
	horizontalStartR = horizontalCap

	# how far are the going to be from the top part of the screen
	# verticalStart is used later to check mouse position in game
	verticalCount = 20
	verticalCap = 20
	verticalStart = verticalCount

	# easy to change variables for the height and width of boxes
	boxW = 150
	boxH = 50

	# Define the class for our square objects
	class Square(pygame.sprite.Sprite):
		def __init__(self, name, position,):
			super(Square, self).__init__()
			
			# Define the dimension of the surface
			self.surf = pygame.Surface((boxW, boxH))
			self.name = name
			self.update_text(name)

			self.rect = self.surf.get_rect(topleft=position)
			
		def update_text(self, name):
			self.surf.fill((225, 225, 225))
			# Define the color of the surface using RGB color coding.
			font = pygame.font.Font(None, 25) # initialize the font
			text_surface = font.render(name, True, (0, 0, 0)) # Choose color for the text (black)
			text_rect = text_surface.get_rect(center=(self.surf.get_width() // 2, self.surf.get_height() // 2)) # center the text
			self.surf.blit(text_surface, text_rect)

	# this will update the score of the user
	def scoreCheck(ans, score):
		if ans:
			return score + 10
		else:
			return score - 5

	# initialize pygame
	pygame.init()

	# Define the dimensions of screen object
	screen = pygame.display.set_mode((1100, 900))

	# Load the Europe map image
	europe_map = pygame.image.load('europe_map3.png')
	# Scale the image to fit the desired dimensions, adjust if necessary
	europe_map = pygame.transform.scale(europe_map, (500, 300))

	world_map = pygame.image.load('World-Country-Map-scaled.jpg')
	world_map = pygame.transform.scale(world_map, (1100,900))

	countries = []  # where we store the countries
	capitals = []   # where we store the capitals
	container = []  # where we store both to latter display them

	score = 0  # keep track of the points the user has

	# Coordinate where the score box will appear (bottom right)
	cornerH = screen.get_height() - 55
	cornerW = screen.get_width() - 155

	keepTrack = Square(str(score), (cornerW, cornerH))  # show the score on the bottom-right of the screen

	
	# Add the countries and capitals to their corresponding list
	for x, y in mydiceuro.items():
		countries.append(x)
		capitals.append(y)

	random.shuffle(countries)
	random.shuffle(capitals)

	#half = (len(mydiceuro) // 2) - 1  # finding the half of the dictionary

	# Populate the container list with country and capital squares
	for x in range(len(mydiceuro)):
		container.append(Square(capitals[x], (horizontalCap, verticalCap)))
		verticalCap += inc
		container.append(Square(countries[x], (horizontalCount, verticalCount)))
		verticalCount += inc
  
	# Set the font of the title
	font = pygame.font.Font(None, 70)
	# Set the title of the game (black)
	title = font.render("Map Master",True,(0,0,0))
	
	# Game variables
	gameOn = True
	countryPressed = False
	capitolPressed = False
	count = 0
	chosen = []
	chosenCountry = []
	chosenCapitol = []
	numPairs = len(mydiceuro)

	inFont = pygame.font.Font(None, 50)
	instructions = font.render("Match the country with the capital",True,(0,0,0))

	# Main game loop
	while gameOn:
		screen.fill((173, 216, 230))  # Clear screen with light blue
		screen.blit(keepTrack.surf, keepTrack.rect)  # Draw score
		screen.blit(europe_map, (screen.get_width() - 500, 250))  # Draw the Europe map on the right side of the screen
		screen.blit(instructions,( 50, cornerH - 100))
		# Display the text on the screen
		screen.blit(title,(cornerW - 200, 100)) # Draw the Title
 

		# Event handling loop
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_BACKSPACE:
					gameOn = False
			elif event.type == QUIT:
				gameOn = False

		# Display the country and capital boxes
		for x in range(len(container)):
			if x not in chosen:
				screen.blit(container[x].surf, container[x].rect)

		# Mouse hover and button click logic
		mouse = pygame.mouse.get_pos()
		blue = (0, 0, 255)
		green = (0, 255, 0)
		black = (0, 0, 0)
		x1 = horizontalStartL
		x2 = horizontalStartR
		y = verticalStart

		# Mouse hover effect for countries and capitals
		for z in range(numPairs):
			# Highlight country box if hovered
			if z not in chosenCountry:
				if x1 <= mouse[0] <= x1 + boxW and y + (z * inc) <= mouse[1] <= y + (z * inc) + boxH:
					pygame.draw.rect(screen, blue, pygame.Rect(x1, y + (z * inc), boxW, boxH), 2)
					if event.type == pygame.MOUSEBUTTONDOWN and count % 2 == 0:
						countryPressed = True
						savedZ = z
						count += 1
			# Highlight capital box if hovered
			if z not in chosenCapitol:
				if x2 <= mouse[0] <= x2 + boxW and y + (z * inc) <= mouse[1] <= y + (z * inc) + boxH:
					pygame.draw.rect(screen, blue, pygame.Rect(x2, y + (z * inc), boxW, boxH), 2)
					if event.type == pygame.MOUSEBUTTONDOWN and count % 2 == 1:
						capitolPressed = True
						savedZ2 = z
						count += 1

		# Logic for country and capital matching
		if countryPressed == True and capitolPressed == False:
			pygame.draw.rect(screen, green, pygame.Rect(x1, y + (savedZ * inc), boxW, boxH), 2)
		elif countryPressed == True and capitolPressed == True:
			pygame.draw.rect(screen, green, pygame.Rect(x2, y + (savedZ2 * inc), boxW, boxH), 2)
			pygame.draw.rect(screen, green, pygame.Rect(x1, y + (savedZ * inc), boxW, boxH), 2)
			pickedCountry = countries[savedZ]
			pickedCapitol = capitals[savedZ2]

			# Check if user got the match right
			if mydiceuro[pickedCountry] == pickedCapitol:
				pygame.draw.rect(screen, black, pygame.Rect(x1, y + (savedZ * inc), boxW, boxH))
				pygame.draw.rect(screen, black, pygame.Rect(x2, y + (savedZ2 * inc), boxW, boxH))
				chosen.append(savedZ * 2 + 1)
				chosenCountry.append(savedZ)
				chosen.append(savedZ2 * 2)
				chosenCapitol.append(savedZ2)
				score = scoreCheck(True, score)
				keepTrack.update_text(str(score))
			else:
				if score != 0:
					score = scoreCheck(False, score)
					keepTrack.update_text(str(score))

			# Reset click flags
			capitolPressed = False
			countryPressed = False
		if len(chosen) == 2 * numPairs:
			screen.fill((173, 216, 230))  # Clear screen with blue
			screen.blit(world_map,(0,0,))
			font = pygame.font.Font(None, 100)
			title = font.render(f'Final Score: {score} / {10*len(mydiceuro)}',True,(0,0,0)) # reuse varible
			screen.blit(title,(cornerW/2 - 250, cornerH - 100)) # Draw the Title
			
		# Update the display
		pygame.display.flip()


# Call the game function to run
if __name__ == "__main__":
    start_capital_game_euro(None)