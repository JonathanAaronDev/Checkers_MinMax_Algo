import pygame
from Constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, BLUE
from game import Game
from minimax.algorithm import alpha_beta_pruning

FPS = 60  # Frames per second (game speed)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Game window
pygame.display.set_caption('Checkers')  # Window title

pygame.font.init()  # Initialize the font module for text rendering

WINNER_FONT = pygame.font.SysFont('comicsans', 100)  # Font used to display the winner

# Function to get the row and column index of a clicked square on the board
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Function to display the winner on the game window
def draw_winner(winner_text, winner):
    if winner == RED:
        text = WINNER_FONT.render(winner_text, True, RED)
    else:
        text = WINNER_FONT.render(winner_text, True, BLUE)

    x = WIDTH // 2 - text.get_width() // 2
    y = HEIGHT // 2 - text.get_height() // 2
    WIN.blit(text, (x, y))  # Draw the winner text on the window

# Main game loop
def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)  # Initialize a new game

    while run:  # Main game loop
        clock.tick(FPS)

        if game.turn == BLUE:  # If it's AI's turn (BLUE)
            # Calculate the best move using the alpha-beta pruning algorithm
            value, new_board = alpha_beta_pruning(game.get_board(), 3, float('-inf'), float('inf'), BLUE, game)
            game.ai_move(new_board)  # Make the AI move

        for event in pygame.event.get():  # Event loop
            if event.type == pygame.QUIT:  # Quit the game if the close button is clicked
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # Handle mouse click events
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)  # Select a square on the board

        game.update()  # Update the game state

        if game.board.winner() is not None:  # If there is a winner
            if game.board.winner() == RED:
                draw_winner("RED WINS!", game.board.winner())
            else:
                draw_winner("BLUE WINS!", game.board.winner())
            pygame.display.update()
            pygame.time.delay(5000)  # Display the winner for 5 seconds
            game.reset()  # Reset the game

    pygame.quit()  # Quit pygame after the main game loop ends

if __name__ == "__main__":
    main()  # Start the game
