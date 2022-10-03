import chess
import random

def get_random_legal_move(board: chess.Board):
    legal_moves = list(board.legal_moves)
    if len(legal_moves) > 0:
        move_selected = random.randint(0, len(legal_moves)-1)
        return legal_moves[move_selected]

def get_square_location(location):
    x = ord(location[0]) - ord('a') + 1
    #print(f"{location[0]}{location[1]}")
    return(f"{x}{location[1]}")