import pygame
from Constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN

class Piece:
    PADDING = 15  # Space between the piece and the border of the square
    OUTLINE = 3  # Outline of the piece

    def __init__(self, row, col, color):
        self.row = row  # Current row of the piece on the board
        self.col = col  # Current column of the piece on the board
        self.color = color  # Color of the piece
        self.king = False  # Boolean to check if the piece is a king
        self.x = 0  # x-coordinate of the piece
        self.y = 0  # y-coordinate of the piece
        self.calc_pos()  # Calculate the current position of the piece

    def calc_pos(self):
        # Method to calculate the position of the piece based on its row and column
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        # Method to make a piece a king
        self.king = True

    def draw(self, win):
        # Method to draw the piece on the window
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)  # Draw the outline of the piece
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)  # Draw the piece
        if self.king:  # Draw the crown if the piece is a king
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        # Method to move a piece to a new position
        self.row = row
        self.col = col
        self.calc_pos()  # Calculate the new position

    def __repr__(self):
        # Method to represent the piece by its color
        return str(self.color)
