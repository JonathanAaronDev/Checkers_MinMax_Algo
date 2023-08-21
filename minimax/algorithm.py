from copy import deepcopy
import pygame

RED = (255, 0, 0)
BLUE = (0, 0, 255)


def alpha_beta_pruning(position, depth, alpha, beta, maximizing_player, game):
    # If we've reached maximum depth or game is finished, return the board score
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    # If it's the maximizing player's turn, try to maximize score
    if maximizing_player:
        max_eval = float('-inf')  # Set initial maximum score to -infinity
        best_move = None  # Best move is initially undefined
        # For each possible move for this position,
        for move in get_all_moves(position, BLUE, game):
            # recursively call alpha-beta pruning to find the score if this move is made
            evaluation = alpha_beta_pruning(move, depth - 1, alpha, beta, False, game)[0]
            # If this move results in a better score, update best_move
            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move
            # Update alpha
            alpha = max(alpha, evaluation)
            # If beta <= alpha, prune branch
            if beta <= alpha:
                break
        return max_eval, best_move

    # If it's the minimizing player's turn, try to minimize score
    else:
        min_eval = float('inf')  # Set initial minimum score to infinity
        best_move = None  # Best move is initially undefined
        # For each possible move for this position,
        for move in get_all_moves(position, RED, game):
            # recursively call alpha-beta pruning to find the score if this move is made
            evaluation = alpha_beta_pruning(move, depth - 1, alpha, beta, True, game)[0]
            # If this move results in a lower score, update best_move
            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move
            # Update beta
            beta = min(beta, evaluation)
            # If beta <= alpha, prune branch
            if beta <= alpha:
                break
        return min_eval, best_move


def simulate_move(piece, move, board, game, skip):
    # Move piece to new location on the board
    board.move(piece, move[0], move[1])
    # If a piece is skipped over, remove it from the board
    if skip:
        board.remove(skip)
    return board


def get_all_moves(board, color, game):
    moves = []  # List to hold all possible moves

    # For each piece on the board of the given color,
    for piece in board.get_all_piece(color):
        valid_moves = board.get_valid_moves(piece)  # Get the valid moves for this piece
        # For each valid move,
        for move, skip in valid_moves.items():
            # Make a temporary copy of the board and simulate the move
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            # Add the new board position to the list of possible moves
            moves.append(new_board)

    return moves  # Return all possible moves
