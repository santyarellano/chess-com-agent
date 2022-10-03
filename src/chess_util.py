import chess
import random

def get_random_legal_move(board: chess.Board):
    legal_moves = list(board.legal_moves)
    move_selected = random.randint(0, len(legal_moves)-1)
    return legal_moves[move_selected]