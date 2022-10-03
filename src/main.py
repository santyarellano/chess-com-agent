import time

from agent import Agent

agent = Agent()

agent.init_window()
agent.start_match_from_main_url()
#match_created = agent.wait_n_secs_for_match_to_start(5)
print(agent.read_board())

# ----- Close the window -----
time.sleep(10)
agent.close_window()