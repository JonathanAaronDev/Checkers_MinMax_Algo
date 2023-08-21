import pygame

# Constants defining the dimensions of the game window and board
WIDTH, HEIGHT = 800, 800  # Window size
ROWS, COLS = 8, 8  # Board size
SQUARE_SIZE = WIDTH // COLS  # Size of a single square on the board

# RGB color definitions for different elements of the game
RED = (255, 0, 0)  # Red pieces
WHITE = (255, 255, 255)  # White squares on the board
BLACK = (0, 0, 0)  # Black squares on the board
BLUE = (0, 0, 255)  # Blue pieces
GREY = (128, 128, 128)  # Gray color for outlines
GREEN = (0, 255, 0)  # Green color for some UI elements (if needed)

# Loading and scaling the crown image that signifies a king piece in the game
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'),(44,25))
