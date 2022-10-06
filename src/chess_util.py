from nis import match
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

def eval_board(fen_board):
    val = 0
    for c in fen_board:
        if c.isalpha():
            piece = 1 if c.isupper() else -1
            letter = c.lower()
            if letter == 'p': # pawn
                piece *= 1
            elif letter == 'n' or letter == 'b': # knight, bishop
                piece *= 3
            elif letter == 'r': # rook
                piece *= 5
            elif letter == 'q': # queen
                piece *= 9
            elif letter == 'k': # king
                piece *= 900
            
            val += piece
    return val

def get_moves_list_at_depth(board: chess.Board, depth: int):
    legal_moves = list(board.legal_moves)
    if len(legal_moves) > 0:
        pass
