import time
import chess

import chess_util

from agent import Agent

agent = Agent()

agent.init_window()
agent.start_match_from_main_url()

# Attempt to start match
attempts_remaining = 5
while attempts_remaining > 0 and not agent.wait_n_secs_for_match_to_start(3):
    print(f"Attempts remaining... {attempts_remaining}")
    agent.click_main_play_btn()
    attempts_remaining -= 1

# Close agent if match was never created
if attempts_remaining == 0:
    agent.close_window()
    quit()

# ----- Game Setup -----
board = chess.Board()
if not agent.is_agent_white():
    board.turn = chess.BLACK

# ----- Start playing -----
while not agent.check_is_game_over():
    if agent.has_turn():
        # update board
        fen = agent.read_board()
        board = chess.Board(fen)
        if not agent.is_agent_white():
            board.turn = chess.BLACK
        
        print(fen)

        # for now we'll play with random legal moves
        selected_move = str(chess_util.get_random_legal_move(board))
        print(selected_move)

        #time.sleep(1.5)
        agent.make_move(selected_move)

        #time.sleep(5)
        #agent.close_window()
        #quit()


# ----- Game Over -----
print('Game over')
time.sleep(5)
agent.close_window()
quit()

# clock-player-turn