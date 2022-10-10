from copy import deepcopy
from nis import match
import chess
import random
import settings

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

def minmax(board: chess.Board, depth: int):
    legal_moves = list(board.legal_moves)

    if len(legal_moves) > 0: 
        best_move = None
        best_move_eval = None
        for move in legal_moves:
            temp_board = deepcopy(board)
            temp_board.push(move)
            fen_temp_board = temp_board.board_fen()
            board_eval = eval_board(fen_temp_board) if depth <= 1 else minmax(temp_board, depth-1)[1]

            if best_move == None:
                best_move_eval = board_eval
                best_move = move
                if depth == settings.minmax_depth:
                    print(f"best future score: {best_move_eval}")

            elif board_eval != None and best_move_eval != None and board_eval != None:
                if (board.turn == chess.WHITE and board_eval > best_move_eval) or (board.turn == chess.BLACK and board_eval < best_move_eval):
                    best_move_eval = board_eval
                    best_move = move
                    if depth == settings.minmax_depth:
                        print(f"best future score: {best_move_eval}")
        
        return [best_move, best_move_eval]

    else:
        return [None, None]