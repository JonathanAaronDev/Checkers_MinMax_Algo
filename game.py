import pygame
from board import Board
from Constants import RED, BLUE, GREEN, SQUARE_SIZE


class Game:
    def __init__(self, win):
        self._init()  # Initialize the game
        self.win = win  # Game window

    def update(self):
        self.board.draw_cubes(self.win)  # Draw the checker board squares
        self.board.draw(self.win)  # Draw the checkers
        self.draw_valid_moves(self.valid_moves)  # Highlight valid moves
        pygame.display.update()  # Update the game window

    def _init(self):
        self.selected = None  # The currently selected checker
        self.board = Board()  # The game board
        self.turn = RED  # The color of the player whose turn it is
        self.valid_moves = {}  # The valid moves for the currently selected checker

    def reset(self):
        self._init()  # Reset the game

    def select(self, row, col):
        # If a checker is already selected, try to move it to the clicked square
        if self.selected:
            result = self._move(row, col)
            if not result:  # If the move is invalid, deselect the checker and try to select a new one
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)  # The checker on the clicked square
        print(piece)
        # If the clicked square contains a checker of the current player, select it
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)  # Get the valid moves for the selected checker
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)  # The checker on the target square
        # If a checker is selected and the target square is a valid move, move the checker
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]  # The checker skipped over (if any)
            if skipped:  # If a checker is skipped over, remove it from the board
                self.board.remove(skipped)
            self.change_turn()  # Change turns after making a move
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        # Draw a circle on all valid move squares
        for move in moves:
            row, col = move
            x = col * SQUARE_SIZE + SQUARE_SIZE // 2
            y = row * SQUARE_SIZE + SQUARE_SIZE // 2
            pygame.draw.circle(self.win, GREEN, (x, y), 15)

    def change_turn(self):
        self.valid_moves = {}  # Clear the valid moves
        # Switch turns
        if self.turn == RED:
            self.turn = BLUE
        else:
            self.turn = RED

    def get_board(self):
        return self.board  # Return the current board state

    def ai_move(self, board):
        self.board = board  # Update the board to the one calculated by the AI
        self.change_turn()  # Change turns after the AI makes a move
