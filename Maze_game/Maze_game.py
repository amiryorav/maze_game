import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Funny Family Maze Game")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw a simple maze (this is just an example)
    pygame.draw.rect(screen, BLACK, (100, 100, 600, 20))
    pygame.draw.rect(screen, BLACK, (100, 100, 20, 400))
    pygame.draw.rect(screen, BLACK, (100, 480, 600, 20))
    pygame.draw.rect(screen, BLACK, (680, 100, 20, 400))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

