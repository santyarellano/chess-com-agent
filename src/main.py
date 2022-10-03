import time
import chess

from agent import Agent

agent = Agent()

agent.init_window()
agent.start_match_from_main_url()

# Attempt to start match
attempts_remaining = 5
while attempts_remaining > 0 and not agent.wait_n_secs_for_match_to_start(10):
    print(f"Attempts remaining... {attempts_remaining}")
    agent.click_main_play_btn()
    attempts_remaining -= 1

# Close agent if match was never created
if attempts_remaining == 0:
    agent.close_window()
    quit()

# Start playing
board = chess.Board()
print(agent.read_board())

time.sleep(5)
agent.close_window()
quit()